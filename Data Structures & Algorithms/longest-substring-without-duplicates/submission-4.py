class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        L, R = 0, 1


        string = s[L]
        best = 1
        while R < len(s):
            if not s[R] in string:
                string += s[R]
                print("String ",string)
                R += 1
            else:
                print("Repetiu ",s[R])
                L += 1
                string = string[1:]
            best = max(best, len(string))
        return best