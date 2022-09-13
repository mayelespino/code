// Calculate md5 sum concurrently
package main

import (
	"bufio"
	"crypto/md5"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

// Parse the signature file, return a map of path->signature
func parseSignaturesFile(path string) (map[string]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	sigs := make(map[string]string)
	scanner := bufio.NewScanner(file)
	for lnum := 1; scanner.Scan(); lnum++ {
		// ae5252a205000e972b9747b0b125cf96  nasa-05.log
		fields := strings.Fields(scanner.Text())
		if len(fields) != 2 {
			return nil, fmt.Errorf("%s:%d bad line", path, lnum)
		}
		sigs[fields[1]] = fields[0]
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return sigs, nil
}

func fileMD5(path string) (string, error) {
	file, err := os.Open(path)
	if err != nil {
		return "", err
	}
	defer file.Close()

	hash := md5.New()
	if _, err := io.Copy(hash, file); err != nil {
		return "", err
	}

	return fmt.Sprintf("%x", hash.Sum(nil)), nil
}

// result type from worker
type result struct {
	path  string
	match bool
	err   error
}

func md5Worker(path string, sig string, out chan *result) {
	r := &result{path: path}
	s, err := fileMD5(path)
	if err != nil {
		r.err = err
		out <- r
		return
	}

	r.match = (s == sig)
	out <- r
}

func main() {
	sigs, err := parseSignaturesFile("md5sum.txt")
	if err != nil {
		log.Fatalf("error: can't read signaure file - %s", err)
	}

	out := make(chan *result)
	for path, sig := range sigs {
		go md5Worker(path, sig, out)
	}

	ok := true
	for range sigs {
		r := <-out
		switch {
		case r.err != nil:
			fmt.Printf("%s: error - %s\n", r.path, r.err)
			ok = false
		case !r.match:
			fmt.Printf("%s: signature mismatch\n", r.path)
			ok = false
		}
	}

	if !ok {
		os.Exit(1)
	}
}
