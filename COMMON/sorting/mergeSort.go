package main

import (
	"fmt"
	"math/rand"
	"time"
)

func populateArray(arrayLen int) []int {
	rand.Seed(time.Now().UnixNano())
	newArray := make([]int, arrayLen)
	for idx,_ := range newArray {
		newArray[idx] = rand.Intn(500)
	}
	return newArray
}

func mergeSort(anArray[] int) []int {
	if(len(anArray) < 2){
		return anArray
	}

	midPoint := len(anArray)/2
	firstHalf := mergeSort(anArray[:midPoint])
	secondHalf := mergeSort(anArray[midPoint:])

	firstLen := len(firstHalf)
	secondLen := len(secondHalf)

	f, s := 0,0
	var mergedArray [] int
	for(f < firstLen && s < secondLen ){
		if firstHalf[f] < secondHalf[s]{
			mergedArray = append(mergedArray, firstHalf[f])
			f += 1
		} else {
			mergedArray = append(mergedArray, secondHalf[s])
			s += 1
		}
	}

	for f < firstLen {
		mergedArray = append(mergedArray, firstHalf[f])
		f += 1
	}

	for s < secondLen {
		mergedArray = append(mergedArray, secondHalf[s])
		s += 1
	}

	return mergedArray
}

func main()  {
	anArray := populateArray(50)
	fmt.Println(anArray)
	anArray = mergeSort(anArray)
	fmt.Println(anArray)
}

