def isPermut(s1,s2):
    return sorted(s1) == sorted(s2)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        L, R = 0,len(s1)
        current = []
        for i in range(R):
            current.append(s2[i])

        while R < len(s2):
            if isPermut(s1, current):
                return True
            current.append(s2[R])
            print(current)
            current.pop(0)
            print(current)
            R += 1
            L += 1
        if isPermut(s1, current):
                return True
        return False

            
            



        
        