class Solution:
    def minSwaps(self, s: str) -> int:
        bal = 0
        for c in s:
            if c == '[':
                bal += 1
            elif bal > 0:
                bal -= 1
        return (bal + 1) // 2