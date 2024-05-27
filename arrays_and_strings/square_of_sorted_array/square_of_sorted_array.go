package main

import (
	"fmt"
	"math"
	"sort"
)

func SortedSquares(arr []int) []int {
	for i := range arr {
		arr[i] *= arr[i]
	}

	sort.Ints(arr)
	return arr
}

func BetterSortedSquares(arr []int) []int {
	n := len(arr)
	res := make([]int, n)
	start, end := 0, n-1
	n--

	for start <= end {
		if math.Abs(float64(arr[start])) < math.Abs(float64(arr[end])) {
			res[n] = arr[end] * arr[end]
			end--
		} else {
			res[n] = arr[start] * arr[start]
			start++
		}
		n--
	}
	return res
}

func main() {
	arr := []int{-4, -1, 0, 3, 10}
	sortedSquares := SortedSquares(arr)

	fmt.Println(sortedSquares)

	newArr := []int{-4, -1, 0, 3, 10}
	betterSortedSquares := BetterSortedSquares(newArr)
	fmt.Println(betterSortedSquares)
}
