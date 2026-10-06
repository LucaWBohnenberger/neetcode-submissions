class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        print(s)
        for i in s:
            if i in "qwertyuioplkjhgfdsazxcvbnm1234567890":
                new_s += i
        t = len(new_s)
        for i in range(t//2):
            if new_s[i] != new_s[t-i-1]:
                return False
        return True
        