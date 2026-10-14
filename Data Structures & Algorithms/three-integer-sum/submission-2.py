class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        esquerda = 0
        direita = len(nums) - 1
        
        lista = []

        for i in range(len(nums)-2):
            val = -nums[i]
            esquerda = i+1
            direita = len(nums) - 1
            while esquerda < direita:
                new_val = nums[esquerda] + nums[direita]
                if new_val == val:
                    lista.append([nums[i], nums[esquerda], nums[direita]])
                    esquerda += 1
                    direita -= 1
                elif new_val > val:
                    direita -= 1
                else:
                    esquerda += 1

        return list(set(tuple(x) for x in lista))