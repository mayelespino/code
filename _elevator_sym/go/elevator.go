package main

import (
	"fmt"
	"strings"
	"time"
)

func elevator(id int, floorChan chan int) {
	for {
		floor := <-floorChan
		floorString := strings.Repeat("-", floor)
		fmt.Println(id, floorString, floor)
	}
}

func main() {
	var fc [5]chan int
	for i := range fc {
		fc[i] = make(chan int)
		go elevator(i, fc[i])
	}

	maxElevators := len(fc) - 1
	var floorNum int
	var elevatorNum int

	for i := range fc {
		fc[i] <- 1
	}

	time.Sleep(time.Second * 1)

	for {
		fmt.Println("Elevator Number: ")
		fmt.Scanf("%d", &elevatorNum)
		if elevatorNum == -1 {
			break
		} else if elevatorNum > maxElevators {
			elevatorNum = maxElevators
		}

		fmt.Println("Floor Number: ")
		fmt.Scanf("%d", &floorNum)
		if floorNum == 0 {
			break
		}
		fc[elevatorNum] <- floorNum
	}
	fmt.Println("done")
}
