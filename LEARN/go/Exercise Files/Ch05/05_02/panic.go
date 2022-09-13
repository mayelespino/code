package main

import (
	"fmt"
)

func main() {
		vals := []int{1, 2, 3}
		// This will cause a panic
		v := vals[10]
		fmt.Println(v)
}
