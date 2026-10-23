class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        water = 0
        best = 0
        while l <= (len(height)-2):
            if height[l] > 0:
                best = l+1
                r = best
                while r < len(height) and height[l] > height[r]:
                    if height[best] < height[r]:
                        best = r
                    if r >= len(height):
                        break
                    r += 1
                if r < len(height):
                    best = r
                    
                remove = 0
                for i in range(l+1, best):
                    remove += height[i]
        
                water += (best-l-1)*min(height[l], height[best]) - remove
                l = best
            else:
                l += 1
            
        return water