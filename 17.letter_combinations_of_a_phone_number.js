/**
 * @param {string} digits
 * @return {string[]}
 */

var letterCombinations = function (digits) {
  if (digits.length == 0) {
    return []
  }

  d = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  }

  // e.g. digits: "23" -> m: [ 'abc', 'def' ]
  const m = []
  for (let digit of digits) {
    m.push(d[digit])
  }

  const r = []
  const path = []

  function backtrack(i) {
    // base case
    if (i >= digits.length) {
      r.push(path.join(""))
      return
    }

    for (let c of m[i]) {
      path.push(c)
      backtrack(i + 1)
      path.pop()
    }
  }

  backtrack(0)
  return r
}

console.log(letterCombinations("23"))
