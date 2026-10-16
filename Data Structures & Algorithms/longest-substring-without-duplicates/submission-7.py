class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maior = 0

        janela = []

        jan = dict()

        for i in range(len(s)):
            if jan.get(s[i], 0) == 0:
                janela.append(s[i])
                jan[s[i]] = 1
            else:
                maior = max(maior, len(janela))
                while jan.get(s[i]) == 1:
                    a = janela.pop(0)
                    del jan[a]
                janela.append(s[i])
                jan[s[i]] = 1

        maior = max(maior, len(janela))
        
        return maior
        