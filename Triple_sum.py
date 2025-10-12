from typing import List

#find all the pair 'a', 'b', 'c' such that a + b + c = 0
#logic: a + b + c = 0 can also be translated as -a = b + c, 
# so if we can set one number as target (-'a') then we only need to find the pair b and c whose sum is equal to -'a'
def triple_sum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    triplets = []
    nums.sort()

    for i in range(n):
        # to prevent duplicate triplets we need to avoid iterating over duplicate 'a' and duplicate 'b'
        # note: we do not need to check for duplicate 'c' values as if 'a' and 'b' are unique the triplet is automatically unique

        #to prevent duplicate 'a' values in triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left = i + 1
        right = n - 1
        pairs = pair_sum_sorted(nums, left, right, target)

        for pair in pairs:
            triplets.append([nums[i]] + pair)
    
    return triplets

def pair_sum_sorted(nums: List[int], left: int, right: int, target: int) -> List[int]:
    pairs = []

    while (left < right):
        if nums[left] + nums[right] == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # to prevent duplicate 'b' values in triplet
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return pairs

input = [0, 0, 1, -1, 1, -1]
print(triple_sum(input))