class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ultima = {}
        inicio = 0
        maior = 0

        for i, c in enumerate(s):
            anterior = ultima.get(c, -1)

            if anterior >= inicio:
                inicio = anterior + 1

            ultima[c] = i

            tamanho = i - inicio + 1
            if tamanho > maior:
                maior = tamanho

        return maior