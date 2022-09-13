// Receiver example
package main

import (
	"fmt"
)

// Point is a 2d point
type Point struct {
	X int
	Y int
}

// Move moves the point
func (p *Point) Move(dx int, dy int) {
	p.X += dx
	p.Y += dy
}

func main() {
	p := &Point{1, 2}
	p.Move(2, 3)
	fmt.Printf("%+v\n", p)
}
