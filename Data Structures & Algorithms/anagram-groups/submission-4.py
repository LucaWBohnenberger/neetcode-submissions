class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aux_strs = strs.copy()
        for i in range(len(strs)):
            aux_strs[i] = sorted(strs[i])

        strs_b = [""] * len(strs)
        for i in range(len(aux_strs)):
            for j in range(len(aux_strs[i])):
                strs_b[i] += aux_strs[i][j]

        visit = set()  # melhor usar set, é mais rápido e evita duplicatas
        retorno = []

        for i in range(len(strs_b)):
            if strs_b[i] in visit:
                continue  # já agrupado antes
            aux = []
            for j in range(len(strs_b)):
                if strs_b[i] == strs_b[j]:
                    aux.append(strs[j])
            retorno.append(aux)
            visit.add(strs_b[i])  # marca o grupo inteiro como visitado

        return retorno
