from typing import List

#find the indices of the numbers in an unsorted array whose sum is the specified target
def par_sum_unsorted(nums: List[int], target: int) -> List[int]:
    
    pairs = {}

    for i in range(len(nums)):
        complementary = target - nums[i]           # num1 + num2 = target can we re-written as num 1 = target - num 2, 
        if complementary in pairs:                 # now we just need to check for num 1 in hashmap whose time complexity is O(1)
            return [i, pairs[complementary]]
        else:
            pairs[nums[i]] = i                     # if the complement (num 1) is not in the hashmap currently, then add num 2 in the hashmap as key with its index as value

input = [-1, 3, 4, 2]
target = 3
print(par_sum_unsorted(input, target))