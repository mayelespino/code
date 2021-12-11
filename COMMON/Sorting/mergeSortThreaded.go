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

    //======

	for {
		select {
		case x, ok := <-leftChannel:
			fmt.Println("leftChannel", x, ok)
			if ok {
                values <- x
			} else {
                close(leftChannel)
                leftChannel = nil
            }
		case x, ok := <-rightChannel:
			fmt.Println("rightChannel", x, ok)
			if ok {
                values <- x
            } else {
                close(rightChannel)
				rightChannel = nil
			}
		}

		if leftChannel == nil && rightChannel == nil {
			break
		}
	}

    //======

    //close(leftChannel)
    //close(rightChannel)    
    close(values)
}

func main() {

    fmt.Println("mergeSortThreaded.go ")

    anArray := populateArray(10)
	fmt.Println(anArray)

    aChannel := make(chan int, 1)

    go mergeSort(anArray, aChannel)

    for value := range aChannel {
        fmt.Println("Right value: ", value)
    }
  
}

// - https://stackoverflow.com/questions/13666253/breaking-out-of-a-select-statement-when-all-channels-are-closed