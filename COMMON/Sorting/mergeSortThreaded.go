package main


import (
    "fmt"
    "time"
    "math/rand"
)


// a very simple function that we'll
// make asynchronous later on
func compute(value int, values chan int) {
    rand_value := rand.Intn(10)
    fmt.Println("Calculated Random Value: {}", rand_value)
    for i := 0; i < value; i++ {
        time.Sleep(time.Second)
        fmt.Println(i)
    }
    values <- rand_value
}

func main() {

    fmt.Println("Goroutine Tutorial")
    values := make(chan int)
    defer close(values)
  
    // sequential execution of our compute function
    go compute(10, values)
    go compute(10, values)

    value := <-values
    fmt.Println(value)
    value = <-values
    fmt.Println(value)

    // we scan fmt for input and print that to our console
    var input string
    fmt.Scanln(&input)

}

