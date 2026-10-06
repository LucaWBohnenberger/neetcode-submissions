class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) -1
        print(people)
        while left <= right:
            value = people[left] + people[right]
            print(value)
            if value > limit:
                count+=1
                right -=1
            else:
                count+=1
                left +=1
                right -=1
            
        return count
