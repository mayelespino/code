package main

import "fmt"

/*
You are given a list of numbers, and garanteed that only one of them occurs an odd number of times.
Find the number which occurs an odd number of times.
 */
import (
	"fmt"
)

func find_odd_number(numbers[]int) int {
	number_map := make(map[int]int)
	for _, number := range numbers {
		_, ok := number_map[number]
		if ok == false{
			number_map[number] = 1
		} else {
			number_map[number] += 1
		}
	}

	for key, value := range number_map{
		if (value % 2) != 0 {
			return(key)
		}
	}
	return(0)
}
func main() {
	numbers := [] int  {1,1,1,9,2,2,1}
	fmt.Println(find_odd_number(numbers))
}
