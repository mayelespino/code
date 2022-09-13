// Example of "switch" statement

package main

import (
	"fmt"
)

func main() {
	x := 2

	switch x {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	default:
		fmt.Printf("many")
	}
	
}
