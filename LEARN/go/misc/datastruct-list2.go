package main

 import (
 	"container/list"
 	"fmt"
 )

 func main() {
 	// create a new link list
 	alist := list.New()

 	fmt.Println("Size before : ", alist.Len()) // list size before

 	// push element into list
 	alist.PushBack("a")
 	alist.PushBack("b")
 	alist.PushBack("c")

 	fmt.Println("Size after insert(push): ", alist.Len()) // list size after

 	// list elements
 	for e := alist.Front(); e != nil; e = e.Next() {
 		fmt.Println(e.Value.(string))
 	}

 	// pop 3 elements
 	alist.Remove(alist.Front())
 	alist.Remove(alist.Front())
 	alist.Remove(alist.Front())

 	fmt.Println("Size after remove(pop) : ", alist.Len()) // list size after

 }