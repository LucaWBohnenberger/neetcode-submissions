class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicionario = dict()

        if len(s1) > len(s2):
            return False

        for i in s1:
            dicionario[i] = dicionario.get(i, 0) + 1
        
        di = dict()
        for i in range(len(s1)):
            di[s2[i]] = di.get(s2[i], 0) + 1

        for letra_id in range(len(s1),len(s2)):
            if dicionario == di:
                return True
            letra_remover = s2[letra_id - len(s1)]
            di[letra_remover] = di.get(letra_remover) - 1
            if di[letra_remover] == 0:
                del di[letra_remover]
            di[s2[letra_id]] = di.get(s2[letra_id], 0) + 1
        
        if dicionario == di:
            return True

        return False