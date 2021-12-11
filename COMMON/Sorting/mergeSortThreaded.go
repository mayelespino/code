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
    for i := 0; i < 10; i++ {
        values <- anArray[i]
    }
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

