class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = len(nums) + 1
        L, R = 0, 0
        
        sub = 0
        while R < len(nums):
            sub += nums[R]

            while sub >= target:
                best = min(best, R - L + 1)
                sub -= nums[L]
                L +=1

            R += 1

        if sub >= target:
            best = min(best, R-L+1)                



        if best == len(nums) + 1:
            return 0
                
                
        return best

        