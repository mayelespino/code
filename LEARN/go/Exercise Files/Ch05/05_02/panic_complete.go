package main

import (
	"fmt"
	//"os"
)

func safeValue(vals []int, index int) int {
	defer func() {
		if err := recover(); err != nil {
			fmt.Printf("ERROR: %s\n", err)
		}
	}()

	return vals[index]
}

func main() {
	/*
		vals := []int{1, 2, 3}
		// This will cause a panic
		v := vals[10]
		fmt.Println(v)
	*/
	/*
		file, err := os.Open("no-such-file")
		if err != nil {
			panic(err)
		}
		defer file.Close()
		fmt.Println("file opened")
	*/

	v := safeValue([]int{1, 2, 3}, 10)
	fmt.Println(v)
}
