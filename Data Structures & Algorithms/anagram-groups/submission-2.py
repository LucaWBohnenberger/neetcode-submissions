from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = defaultdict(list)
        for s in strs:
            chave = "".join(sorted(s))
            grupos[chave].append(s)
        return list(grupos.values())
  

        return retorno

     