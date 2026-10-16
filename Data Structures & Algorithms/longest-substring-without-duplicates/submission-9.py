class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maior = 0
        inicio = 0
        ultima_posicao = {}

        for i, caractere in enumerate(s):
            if caractere in ultima_posicao:
                inicio = max(inicio, ultima_posicao[caractere] + 1)

            ultima_posicao[caractere] = i
            maior = max(maior, i - inicio + 1)

        return maior