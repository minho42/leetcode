// https://leetcode.com/problems/generate-parentheses/description/

// Input: n = 3
// Output: ["((()))","(()())","(())()","()(())","()()()"]

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const r = []
  function backtrack(path, lc, rc) {
    // base cases
    if (rc > lc) {
      return
    }
    if (path.length === n * 2) {
      r.push(path.join(""))
      return
    }

    // go left
    if (lc < n) {
      path.push("(")
      backtrack(path, lc + 1, rc)
      path.pop()
    }

    // go right
    if (rc < n) {
      path.push(")")
      backtrack(path, lc, rc + 1)
      path.pop()
    }
  }

  backtrack([], 0, 0)
  return r
}

console.log(generateParenthesis(3))
// console.log(generateParenthesis(6))
