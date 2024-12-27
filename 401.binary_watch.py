# https://leetcode.com/problems/binary-watch/description/

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]


from typing import List


# Topics
# Backtracking
# Bit Manipulation


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        r = []

        hms = [
            "h8",
            "h4",
            "h2",
            "h1",
            "m32",
            "m16",
            "m8",
            "m4",
            "m2",
            "m1",
        ]

        def convert_to_time_str(arr: List[str]) -> str | None:
            h = sum([(int(a[1:])) for a in arr if a[0] == "h"])
            m = sum([(int(a[1:])) for a in arr if a[0] == "m"])

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
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
print(s.readBinaryWatch(8))
print(s.readBinaryWatch(9))
