// channels
package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)

	// This will block
		<-ch
		fmt.Println("Here")
}
