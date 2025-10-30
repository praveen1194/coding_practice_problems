from typing import List

#find the indecies of the pair in a sorted array whose sum is equal to the target
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums)-1

    while (left < right):
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1


nums = [-5,-2,3,4,6]
target = 7

print(pair_sum_sorted(nums, target))