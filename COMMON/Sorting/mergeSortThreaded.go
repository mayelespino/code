package main


import (
    "fmt"
    "time"
    "math/rand"
)


func populateArray(arrayLen int) []int {
	rand.Seed(time.Now().UnixNano())
	newArray := make([]int, arrayLen)
	for idx,_ := range newArray {
		newArray[idx] = rand.Intn(500)
	}
	return newArray
}

// 
func mergeSort(anArray[] int, values chan int) {
	if(len(anArray) < 2){
        values <- anArray[0]
        close(values)
		return 
	}

	midPoint := len(anArray)/2
    leftChannel := make(chan int, 1)
    rightChannel := make(chan int, 1)
	go mergeSort(anArray[:midPoint], leftChannel)
	go mergeSort(anArray[midPoint:], rightChannel)

    var firstHalf[] int
    var secondHalf[] int

    for value := range leftChannel {
        firstHalf = append(firstHalf, value)
    }

    for value := range rightChannel {
        secondHalf = append(secondHalf, value)
    }

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

    for _, number := range mergedArray {
        values <- number
    }

    //======
    close(values)
}

func main() {

    fmt.Println("mergeSortThreaded.go ")

    anArray := populateArray(999)
	fmt.Println(anArray)
    fmt.Println("\n\n==\n\n")

    aChannel := make(chan int, 1)

    go mergeSort(anArray, aChannel)

    var sortedArray [] int
    for value := range aChannel {
        sortedArray = append(sortedArray, value)
    }
	fmt.Println(sortedArray)
    fmt.Println("\n\n==")
  
}

// - https://stackoverflow.com/questions/13666253/breaking-out-of-a-select-statement-when-all-channels-are-closed