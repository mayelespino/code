package main

import (
	"fmt"
	"time"
)

func elevator(id int, floorChan chan int) {
	for {
		floor := <-floorChan
		fmt.Println(id, floor)
	}
}

func main() {
	fc1 := make(chan int)
	fc2 := make(chan int)
	go elevator(1, fc1)
	go elevator(2, fc2)
	fc1 <- 2
	fc2 <- 1
	var floorNum int

	for {
		fmt.Scanf("%d", &floorNum)
		fc1 <- floorNum
		fc2 <- floorNum
		if floorNum == 0 {
			break
		}
	}
	time.Sleep(time.Millisecond * 1000)
	fmt.Println("done")
}
