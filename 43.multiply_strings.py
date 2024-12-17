# https://leetcode.com/problems/multiply-strings/description/

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


def multiply(num1: str, num2: str) -> str:
    return str(int(num1) * int(num2))


print(multiply("2", "3"))
print(multiply("123", "456"))
