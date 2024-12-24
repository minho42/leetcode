// https://leetcode.com/problems/valid-parentheses/description/

package main

import "fmt"

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
	fmt.Println(isValid("([)]"))
}

func isValid(s string) bool {
	if len(s)%2 == 1 {
		return false
	}

	if count('(', s) != count(')', s) ||
		count('[', s) != count(']', s) ||
		count('{', s) != count('}', s) {
		return false
	}

	stack := []int{}
	for i := 0; i < len(s); i++ {
		if len(stack) == 0 {
			stack = append(stack, i)
			continue
		}
		pi := stack[len(stack)-1]
		stack = append(stack, i)
		if (s[pi] == '(' && s[i] == ')') ||
			(s[pi] == '[' && s[i] == ']') ||
			(s[pi] == '{' && s[i] == '}') {
			stack = stack[:len(stack)-2]
		}
	}

	return len(stack) == 0
}

func count(c rune, s string) int {
	count := 0
	for _, v := range s {
		if v == c {
			count++
		}
	}
	return count
}
