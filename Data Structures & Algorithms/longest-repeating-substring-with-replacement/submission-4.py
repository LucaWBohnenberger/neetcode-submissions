class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        const = {}

        L, R = 0,0
        best = 0
        while R < len(s):
            if s[R] in const.keys():
                const[s[R]] += 1
            else:
                const[s[R]] = 1

            print(R-L , " - ", max(const.values()))
            while (R-L+1)-max(const.values()) > k:
                const[s[L]] -= 1
                L += 1
            print("Depois: ", (R-L)-max(const.values()))
            
            best = max(best, R-L+1)
            R += 1

        return best
            
            

            

        