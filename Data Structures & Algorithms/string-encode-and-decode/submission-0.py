class Solution:

    def encode(self, strs: List[str]) -> str:
        lista = ""
        for i in strs:
            lista += i + "...|..."
        return lista

    def decode(self, s: str) -> List[str]:
        lista = s.split("...|...")
        lista.pop(-1)
        return lista