class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            num = ""
            for j in range(len(nums)):
                if i != j:
                    if num == "":
                        num = nums[j]
                    else:
                        num *= nums[j]
            ret.append(num)
        return ret
        