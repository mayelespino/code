package main

import (
	"fmt"
)

func isWord( cWord[]int32, words[] string) bool {
	cW := string(cWord)
	for _,w := range(words) {
		if (cW == w) {
			return true
		}
	}
	return(false)
}

func canSeparateStringInToWords( originalString string, words[] string ) bool{
	var word = [] int32 {}
	wasFound := false
	for _, cchar := range originalString {
		word = append(word, cchar)
		wasFound = isWord(word, words)
		if wasFound {
			word = word[:0]
		}
	}
	return wasFound

}

func separateStringInToWords( originalString string, words[] string ) [] string{
	var word = [] int32 {}
	wasFound := false
	var sliceOfWords = [] string {}
	for _, cchar := range originalString {
		word = append(word, cchar)
		wasFound = isWord(word, words)
		if wasFound {
			sliceOfWords = append(sliceOfWords, string(word))
			word = word[:0]
		}
	}
	if wasFound {
		return sliceOfWords
	} else {
		return [] string {}
	}

}

func main() {
	sourceString := "applecart"
	words := []string {"apple","cart", "new", "my"}
	fmt.Println(sourceString, "<-->",words)
	fmt.Println(canSeparateStringInToWords(sourceString, words))
	fmt.Println(separateStringInToWords(sourceString, words))
	fmt.Println("=====")

	sourceString = "blaapplecart"
	fmt.Println(sourceString, "<-->",words)
	fmt.Println(canSeparateStringInToWords(sourceString, words))
	fmt.Println(separateStringInToWords(sourceString, words))
	fmt.Println("=====")

	sourceString = "newapplecart"
	fmt.Println(sourceString, "<-->",words)
	fmt.Println(canSeparateStringInToWords(sourceString, words))
	fmt.Println(separateStringInToWords(sourceString, words))
	fmt.Println("=====")
}
