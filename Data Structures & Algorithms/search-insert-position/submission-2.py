class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        L, R = 0, len(nums) - 1
        mid = 0
        res = len(nums)
        while L <= R :
            mid = (L+R)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
        

        
        return res
            
        
            
        