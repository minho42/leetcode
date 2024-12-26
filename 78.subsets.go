// https://leetcode.com/problems/subsets/

// ref: https://youtu.be/L0NxT2i-LOY?si=BcQ29Dfw-qfRka7q

package main

import "fmt"

func subsets(nums []int) [][]int {
	r := [][]int{}
	sol := []int{}

	// inner function
	var backtrack func(int)
	backtrack = func(i int) {
		// base case
		if i == len(nums) {
			r = append(r, append([]int{}, sol...))
			return
		}

		// don't pick
		backtrack(i + 1)

		// pick
		sol = append(sol, nums[i])
		backtrack(i + 1)
		sol = sol[:len(sol)-1]
	}

	backtrack(0)
	return r
}

func main() {
	fmt.Println(subsets([]int{1, 2, 3}))
}
