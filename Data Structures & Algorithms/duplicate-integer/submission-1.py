class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = set()
        for i in nums:
            if not i in aux:
                aux.add(i)
            else:
                return True
        return False
        