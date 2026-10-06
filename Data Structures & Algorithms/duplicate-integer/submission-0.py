class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = []
        for i in nums:
            if not i in aux:
                aux.append(i)
            else:
                return True
        return False
        