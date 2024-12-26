// https://leetcode.com/problems/subsets/

// ref: https://youtu.be/L0NxT2i-LOY?si=BcQ29Dfw-qfRka7q

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsets = function (nums) {
  const r = []
  const sol = []

  function backtrack(i) {
    //base case
    if (i === nums.length) {
      r.push([...sol])
      return
    }

    // don't pick
    backtrack(i + 1)

    // pick
    sol.push(nums[i])
    backtrack(i + 1)
    sol.pop()
  }

  backtrack(0)
  return r
}

console.log(subsets([1, 2, 3]))
