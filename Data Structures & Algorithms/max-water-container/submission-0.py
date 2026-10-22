class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        dist = r - l

        best = max(0, min(heights[l], heights[r]) * (r-l))

        while r != l:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            best = max(best, min(heights[l], heights[r]) * (r-l))

        return best

            
        