// https://leetcode.com/problems/two-sum/description/

// nums = [3,3]
// target = 6

// nums = [-1,-2,-3,-4,-5]
// target = -8

package main

import "fmt"

func two_sum(nums []int, target int) []int {
	h := make(map[int]int)

	for i, v := range nums {
		h[v] = i
	}
	
	for i, n := range nums {
		x := target - n
		if j, exists := h[x]; exists && i != j {
			return []int{i,j}
		}
	}
	
	return nil	
}

func main() {
	nums := []int{-1,-2,-3,-4,-5}
	target := -8
	
	fmt.Println(two_sum(nums, target))
}