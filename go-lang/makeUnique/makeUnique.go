//
// Interview question for Apple watch triage-tools interview
//
package main

import (
	"fmt"
	"os"
	"sort"
)

func main() {
	argsWithoutProg := os.Args[1:]
	var mapArgs = make(map[string]int)

	for _, item := range argsWithoutProg {
		_, ok := mapArgs[item]
		if ok {
			mapArgs[item] += 1
		} else {
			mapArgs[item] = 1
		}
	}

	// print the map with uniqe values and times it occurs.
	for key, value := range mapArgs {
		fmt.Println("Key:", key, "Occurs:", value, "Times.")
	}

	// print the list in the order that it was given
	uniqueArray := []string{}
	var currentItem= argsWithoutProg[0]
	uniqueArray = append(uniqueArray, currentItem)

	fmt.Println(" Uniqued list: ")
	fmt.Print(currentItem, " ")
	for _, item := range argsWithoutProg[1:] {
		if item != currentItem {
			fmt.Print(item, " ")
			uniqueArray = append(uniqueArray, item)
		}
		currentItem = item
	}

	sort.Strings(uniqueArray)
	fmt.Println(" ")
	fmt.Println("Sorted unique array:")
	for _, item := range uniqueArray {
		fmt.Print(item, " ")
	}
}
