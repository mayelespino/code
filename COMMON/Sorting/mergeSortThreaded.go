package main


import (
    "fmt"
    "time"
)


// a very simple function that we'll
// make asynchronous later on
func compute(value int, values chan int) {
    value := rand.Intn(10)
    fmt.Println("Calculated Random Value: {}", value)
    for i := 0; i < value; i++ {
        time.Sleep(time.Second)
        fmt.Println(i)
    }
    values <- value
}

func main() {

    fmt.Println("Goroutine Tutorial")
    values := make(chan int)
    defer close(values)
  
    // sequential execution of our compute function
    go compute(10)
    go compute(10)

    value := <-values
    fmt.Println(value)

    // we scan fmt for input and print that to our console
    var input string
    fmt.Scanln(&input)

}

