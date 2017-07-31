package main

import (
    "bufio"
    "io"
    "strings"
    "os"
    "fmt"
    "sort"
)

var bigBuf string 
var wordCount = make(map[string]int)

func sortAndPrintArray(inMap map[string]int) int {
    var revMap = make(map[int]string)
    for k, v  := range inMap {
        revMap[v] = k
    }
    //for k, v  := range revMap {
    //    fmt.Println("Key:", k, "Value:", v)
    //}
    var keys []int
    for k, _ := range revMap {
        keys = append(keys, k)
    }
    sort.Ints(keys)
    limit := len(revMap) - 10
    idx := 0
    for _, k :=  range keys {
        idx++
        if idx > limit{
            fmt.Println("Key:", k, "Value:", revMap[k])
        }
    }
    return(0)
}

func readAndProcessBuf(inBuf []byte, inMap map[string]int) string {
    tmpString := string(inBuf)
    tmpString = strings.Replace(tmpString, "'", " ", -1)
    tmpString = strings.Replace(tmpString, ".", " ", -1)
    tmpString = strings.Replace(tmpString, ",", " ", -1)
    tmpString = strings.Replace(tmpString, ";", " ", -1)
    tmpString = strings.Replace(tmpString, "\"", " ", -1)
    tmpString = strings.Replace(tmpString, "(", " ", -1)
    tmpString = strings.Replace(tmpString, ")", " ", -1)
    tmpString = strings.Replace(tmpString, "\n", " ", -1)
    tmpString = strings.Replace(tmpString, "?", " ", -1)
    tmpString = strings.Replace(tmpString, "!", " ", -1)
    tmpString = strings.Replace(tmpString, "-", " ", -1)
    tmpString = strings.Replace(tmpString, "_", " ", -1)
    tmpString = strings.Replace(tmpString, "=", " ", -1)
    tmpString = strings.Replace(tmpString, "#", " ", -1)
    tmpString = strings.ToLower(tmpString)
    words := strings.Split(tmpString, " ")
    for i := 0; i < len(words); i += 1 {
        _, ok := inMap[words[i]]
        if ok {
            inMap[words[i]] += 1
        } else {
            inMap[words[i]] = 1
        }
    }
    return(tmpString)
}

func main() {
    r := bufio.NewReader(os.Stdin)
    buf := make([]byte, 0, 4*1024)
    for {
        n, err := r.Read(buf[:cap(buf)])
        buf = buf[:n]
        if n == 0 {
            if err == nil {
                continue
            }
            if err == io.EOF {
                break
            }
            fmt.Println(err)
        }
        if err != nil && err != io.EOF {
            fmt.Println(err)
        }
        // process buf
        bigBuf += readAndProcessBuf(buf, wordCount)
    }
    fmt.Println("Top 10:")
    sortAndPrintArray(wordCount)
    fmt.Println("Done")
}
