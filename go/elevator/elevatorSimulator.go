package main

import (
	"fmt"
	"strings"
	"time"
)

func elevator(c chan int, elevatorNumber int) {
	currentFloor := 1
	for {
		floor := <- c
		diff := currentFloor - floor
		if diff < 0 {
			diff = -(diff)
		}
		time.Sleep(time.Second * time.Duration(diff))
		currentFloor = floor
		elevatorStr := strings.Repeat("=", floor)
		fmt.Printf("\n[%d]%s>%d\n", elevatorNumber, elevatorStr, floor)
	}
} //func elevator

func main() {
	var chans [5]chan int
	for i := range chans {
		chans[i] = make(chan int)
		go elevator(chans[i], i)
	}

	lastElevator := (len(chans))-1
	for {
		fmt.Println("\nElevator number:")
		var elevator int
		fmt.Scanln(&elevator)
		if elevator < 0 {
			fmt.Print("Exiting!\n")
			break
		} else if elevator > lastElevator {
			fmt.Printf("requested elevator: %d, setting to last elevator: %d", elevator, lastElevator)
			elevator = lastElevator
		}

		fmt.Println("\nFloor")
		var floor int
		fmt.Scanln(&floor)
		if floor < 1 {
			floor = 1
		} else if floor > 100 {
			fmt.Println("0 > Floor <= 100")
			floor = 100
		}
		chans[elevator] <- floor
		time.Sleep(time.Second * 1)
	}
}