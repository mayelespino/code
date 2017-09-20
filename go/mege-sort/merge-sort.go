package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	array_random_ints := random_list(10)

	fmt.Println("\n\nUnordered list:")
	for _, element := range array_random_ints {
		fmt.Print(element)
		fmt.Print(" ")
	}

	sorted_list := merge_sort(array_random_ints)
	fmt.Println("\nSorted list:")
	for _, element := range sorted_list {
		fmt.Print(element)
		fmt.Print(" ")
	}
	fmt.Println("\n")
}

func random_list(l int) []int {
	list := make([]int, l)
	for i := 0; i < l; {
		list[i] = randInt(0, 1000)
		i++
	}
	return(list)
}

func randInt(min int, max int) int {
	rand.Seed(time.Now().UTC().UnixNano())
	return min + rand.Intn(max-min)
}

func merge_sort(list_to_sort []int) []int {
	if len(list_to_sort) < 2 {
		return(list_to_sort)
	}

	half := len(list_to_sort)/2
	first_half := list_to_sort[:half]
	second_half := list_to_sort[half:]

	part_a := merge_sort(first_half)
	part_b := merge_sort(second_half)

	result_list := make([]int, len(part_a) + len(part_b))

	idx_a := 0
	idx_b := 0
	idx_r := 0

	for  {
		if part_a[idx_a] > part_b[idx_b]{
			result_list[idx_r] = part_a[idx_a]
			idx_a++
		} else {
			result_list[idx_r] = part_b[idx_b]
			idx_b++
		}

		idx_r++

		if len(part_a) == idx_a || len(part_b) == idx_b {
			break
		}
	}

	if len(part_a) > idx_a {
		for {
			result_list[idx_r] = part_a[idx_a]
			idx_a++
			idx_r++
			if len(part_a) == idx_a {break}
		}
	}
	if len(part_b) > idx_b {
		for {
			result_list[idx_r] = part_b[idx_b]
			idx_b++
			idx_r++
			if len(part_b) == idx_b {
				break
			}
		}
	}

	return (result_list)
}
