from typing import List

def par_sum_unsorted(nums: List[int], target: int) -> List[int]:
    
    pairs = {}

    for i in range(len(nums)):
        complementary = target - nums[i]
        if complementary in pairs:
            return [i, pairs[complementary]]
        else:
            pairs[nums[i]] = i

input = [-1, 3, 4, 2]
target = 3
print(par_sum_unsorted(input, target))