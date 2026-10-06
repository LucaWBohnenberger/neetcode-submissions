class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pointer1 = 0;
        int pointer2 = numbers.size() - 1;

        while (numbers[pointer1] + numbers[pointer2] != target){
            if (numbers[pointer1] + numbers[pointer2] < target){
                pointer1++;
            }else{
                pointer2--;
            }
        }
        return {++pointer1, ++pointer2};
    }
};
