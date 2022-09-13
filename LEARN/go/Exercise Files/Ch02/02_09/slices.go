// Go slices
package main

import (
	"fmt"
)

func main() {
	// Same type
	loons := []string{"bugs", "daffy", "taz"}
	fmt.Printf("loons = %v (type %T)\n", loons, loons)

	// Length
	fmt.Println(len(loons)) // 3

	fmt.Println("----")
	// 0 indexing
	fmt.Println(loons[1]) // daffy

	fmt.Println("----")
	// slices
	fmt.Println(loons[1:]) // [daffy taz]

}
