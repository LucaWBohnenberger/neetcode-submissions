
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lista = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            esquerda = i + 1
            direita = n - 1

            while esquerda < direita:
                soma = nums[i] + nums[esquerda] + nums[direita]

                if soma == 0:
                    lista.append([nums[i], nums[esquerda], nums[direita]])
                    esquerda += 1
                    direita -= 1

                    while esquerda < direita and nums[esquerda] == nums[esquerda - 1]:
                        esquerda += 1

                    while esquerda < direita and nums[direita] == nums[direita + 1]:
                        direita -= 1

                elif soma < 0:
                    esquerda += 1
                else:
                    direita -= 1

        return lista
