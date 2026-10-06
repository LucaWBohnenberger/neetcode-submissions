class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = []
        L, R = 0, k 
        for i in range(k):
            closest.append(arr[i])
    
        while R < len(arr):
            if abs(arr[R] - x) > abs(closest[0] - x) or (abs(arr[R] - x) == abs(closest[0] - x) and arr[R] > closest[0]):
                break
            closest.append(arr[R])
            closest.pop(0)
            R += 1
            L += 1
        return closest