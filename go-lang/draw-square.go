package main 

import ( 
    "code.google.com/p/go-tour/pic" 
    "image" 
    "image/color" 
) 

func main() { 
    m := image.NewRGBA(image.Rect(0, 0, 100, 100)) 
    for x := 20; x < 80; x++ { 
        y := x/3 + 15 
        m.Set(x, y, color.Black) 
    } 
    pic.ShowImage(m) 
} 