# https://leetcode.com/problems/binary-watch/description/

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]


# topic: backtracking, bit manupilation

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        r = []

        hms = [
            "h3",
            "h2",
            "h1",
            "h0",
            "m5,",
            "m4,",
            "m3",
            "m2",
            "m1",
            "m0",
        ]

        def convert_to_time_str(arr):
            # h0 => 2 ** 0 => 1
            # m1 => 2 ** 1 => 2
            if len(arr) != turnedOn:
                return None
            h = 0
            m = 0
            for a in arr:
                if a[0] == "h":
                    h += 2 ** int(a[1])
                else:
                    m += 2 ** int(a[1])

            if h > 11 or m > 59:
                return None

            return f"{str(h)}:{str(m).rjust(2,'0')}"

        def backtrack(start, path):
            # base case
            if len(path) == turnedOn:
                r.append(path[:])
                return

            # recursion
            for i in range(start, len(hms)):
                path.append(hms[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        r = [(convert_to_time_str(x)) for x in r]
        r = [x for x in r if x is not None]
        return sorted(list(set(r)))


s = Solution()
# print(s.readBinaryWatch(1))
# print(s.readBinaryWatch(2))
print(s.readBinaryWatch(8))
# print(s.readBinaryWatch(9))
