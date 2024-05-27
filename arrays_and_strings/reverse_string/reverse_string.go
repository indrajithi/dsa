package main

import "fmt"

// reverseString reverses the given slice of bytes in place
func reverseString(s []byte) {
	start := 0
	end := len(s) - 1

	for start < end {
		s[start], s[end] = s[end], s[start]
		start++
		end--
	}
}

func main() {
	s := []byte("hello!")
	reverseString(s)
	fmt.Println(s)
	fmt.Println(string(s))
}
