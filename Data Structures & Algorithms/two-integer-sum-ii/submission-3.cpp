class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pointer1 = 0;
        int pointer2 = numbers.size() - 1;

        int sum = numbers[pointer1] + numbers[pointer2];

        while (sum != target){
            if (sum < target){
                pointer1++;
            }else{
                pointer2--;
            }

            sum = numbers[pointer1] + numbers[pointer2];
        }
        return {++pointer1, ++pointer2};
    }
};
