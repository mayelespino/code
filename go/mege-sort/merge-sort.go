package main

import (
	//"fmt"
	"math/rand"
	"time"
)

func main() {
	//fmt.Println(random_list(10))
	random_list(10)
}

func random_list(l int) []int {
	list := make([]int, l, l)
	for i := 0; i < l; {
		list[i] = randInt(0, 1000)
		i++
	}
	return(list)
}

func randInt(min int, max int) int {
	rand.Seed(time.Now().UTC().UnixNano())
	return min + rand.Intn(max-min)
}