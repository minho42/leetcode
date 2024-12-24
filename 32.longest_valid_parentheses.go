package main

import "fmt"

func main() {
	fmt.Println(longestValidParentheses("()(()))())("))
}

// ref: https://youtu.be/r0-zx5ejdq0?si=l18n5DzhEXdNNiac

func longestValidParentheses(s string) int {
	stack := []int{-1}
	m := 0

	for i := 0; i < len(s); i++ {
		si := stack[len(stack)-1]
		stack = append(stack, i)
		if si >= 0 && s[si] == '(' && s[i] == ')' {
			// fmt.Println(m, stack)
			endIndex := len(stack) - 2
			stack = stack[:endIndex]
			m = max(m, i-stack[len(stack)-1])
		}
	}
	return m
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
