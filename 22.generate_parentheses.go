package main

import (
	"fmt"
	"strings"
)

func generateParenthesis(n int) []string {
	r := []string{}

	var backtrack func(path []string, lc int, rc int)
	backtrack = func(path []string, lc int, rc int) {
		// base cases
		if rc > lc {
			return
		}
		if len(path) == n*2 {
			r = append(r, strings.Join(path, ""))
			return
		}

		// go left
		if lc < n {
			path = append(path, "(")
			backtrack(path, lc+1, rc)
			path = path[:len(path)-1]
		}

		// go right
		if rc < n {
			path = append(path, ")")
			backtrack(path, lc, rc+1)
			path = path[:len(path)-1]

		}
	}

	backtrack([]string{}, 0, 0)
	return r
}

func main() {
	fmt.Println(generateParenthesis(3))
}
