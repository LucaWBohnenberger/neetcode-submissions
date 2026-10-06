class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        L, R = 0, k-1

        best = max(nums)

        while R < len(nums):
            diff = abs(nums[L] - nums[R])
            best = min(best,diff)
            L+=1
            R+=1
        return best

