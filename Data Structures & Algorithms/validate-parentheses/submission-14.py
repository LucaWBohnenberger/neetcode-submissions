class Solution:
    def isValid(self, s: str) -> bool:
        dicionario = {"[":"]", "{":"}", "(":")"}
        
        next = []

        if len(s) <= 1 or s[0] in dicionario.values():
            return False

        for term in s:
            if term in dicionario.keys():
                next.append(dicionario[term])
            else:
                print(next)
                print(term, "--", "opa")
                if len(next) == 0 or next[-1] != term:
                    return False
                else:
                    next.pop()
        if len(next) == 0:
            return True
        else:
            return False
        