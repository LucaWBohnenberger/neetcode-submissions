class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        array = sorted(set_)
        print(set_)
        print(array)
        count = 0
        maxValue = 0
        for i in range(len(array)):
            count = 1
            j = 1
            while(True):
                if i+j >= len(array):
                    print("Finzalizou por tamanho")
                    break
                if array[i+j] == array[i]+j:
                    print("i: ", i, "  j:", j, "  valor: ", array[i+j], " ", array[i]+j)
                    count +=1
                else:
                    print("Finalizou por não ser sequencia",array[i+j], " ", array[i]+j )
                    break
                j +=1
            maxValue = max(maxValue, count)
        return maxValue