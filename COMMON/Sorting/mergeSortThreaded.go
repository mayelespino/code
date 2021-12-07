package main


import (
    "fmt"
    "time"
    "math/rand"
)


// a very simple function that we'll
// make asynchronous later on
func compute(value int, values chan int) {
    for i := 0; i < value; i++ {
        time.Sleep(time.Second)
        values <- rand.Intn(10)
    }
    
}

func main() {

    fmt.Println("Goroutine Tutorial: 2 ")
    right_values := make(chan int, 10)
    defer close(right_values)
    left_values := make(chan int, 10)
    defer close(left_values)
  
    // sequential execution of our compute function
    go compute(10, right_values)
    go compute(10, left_values)

    for i := 0; i < 10; i++ {
        value := <-right_values
        fmt.Println("First from channel: ", value)
    }

    for i := 0; i < 10; i++ {
        value := <-left_values
        fmt.Println("Second from channel: ", value)
    }

}

