class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        reversed_digits = digits[::-1]
        return reversed_digits == digits