class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            new_s = replace(s,i, "")
            print(s[i])
            if palindrome(new_s):
                return True
        return palindrome(s)



def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def replace(string, sub_pos, add):
    new_string=""
    for i in range(len(string)):
        if i != sub_pos:
            new_string += string[i]
    return new_string



        