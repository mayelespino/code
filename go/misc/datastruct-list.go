package main

import "fmt"

type node struct {
    name string
    next *node
    prev *node
}

func main() {
	fmt.Println("Start")
	first := node{"First", nil, nil}
	second := node{"Second", nil, &first}
	third := node {"third", nil, &second}
	
	fmt.Println(third.name)
	current := third.prev
	fmt.Println(current.name)
	fmt.Println((*third.prev).name)
}

