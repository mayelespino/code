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
func compute(value int, values chan int) {
    for i := 0; i < 5; i++ {
        time.Sleep(time.Second)
        values <- rand.Intn(value)
    }
    //close(values)    
}

func main() {

    fmt.Println("Goroutine Tutorial: 2 ")
    right_values := make(chan int, 1)
    defer close(right_values)
    left_values := make(chan int, 1)
    defer close(left_values)
  
    // sequential execution of our compute function
    go compute(9, right_values)
    go compute(90, left_values)

    for value:= range right_values {
        fmt.Println("Right value: ", value)
    }
    close(right_values)

    for value:= range left_values {
        fmt.Println("Left value: ", value)
    }
    close(right_values)

}

