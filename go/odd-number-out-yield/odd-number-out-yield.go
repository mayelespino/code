package main

import "fmt"

/*
You are given a list of numbers, and garanteed that only one of them occurs an odd number of times.
Find the number which occurs an odd number of times.
 */

func find_odd_number_yield(numbers[]int) chan int {
	yield := make (chan int);
	number_map := make(map[int]int)
	for _, number := range numbers {
		_, ok := number_map[number]
		if ok == false{
			number_map[number] = 1
		} else {
			number_map[number] += 1
		}
	}

	go func ()  {
		for key, value := range number_map{
			if (value % 2) != 0 {
				yield <- key
			}
		}
	} ();
	return yield
}


func main() {
	numbers := [] int  {1,1,1,9,2,2,1,7,8,8,8}
	fmt.Println("--")
	list := find_odd_number_yield(numbers)
	bar := <- list
	fmt.Println(bar)
}
