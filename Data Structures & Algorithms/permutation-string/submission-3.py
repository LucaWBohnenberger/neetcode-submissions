class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)

        L, R = 0,len(s1)
        s1_table = {}
        for i in s1:
            s1_table[i] = 1 + s1_table.get(i,0)
        current = {}
        for i in range(R):
            current[s2[i]] = 1 + current.get(s2[i],0)


        while R < len(s2):
            if s1_table == current:
                return True
            current[s2[R]] = 1 + current.get(s2[R],0)
            current[s2[L]] -= 1
            if current[s2[L]] == 0:
                del current[s2[L]]
            R += 1
            L += 1
        if s1_table == current:
                return True
        return False

            
            



        
        