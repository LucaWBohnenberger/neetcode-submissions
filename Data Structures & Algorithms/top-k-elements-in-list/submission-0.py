class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lista = {}
        nums = sorted(nums)
        count = 0
        aux = nums[0]

        for i in range(len(nums)):
            if nums[i] == aux:
                count += 1
            else:
                lista[aux] = count
                aux = nums[i]
                count = 1
        lista[aux] = count  # adiciona o último elemento

        # pega os k mais frequentes
        terms = sorted(lista, key=lista.get, reverse=True)[:k]
        return terms