from typing import List

#Given a list of heights of vertical lines, such that when placed in the provided sequence in x-axis can hold water,
# find the pair that can hold the most amount of water and return the amount of water it holds
def find_larget_container(nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    max_qty = 0

    while left < right:
        #formula to calculate the area, the maximum height water can go upto is limited by the shortest values in the pair or the water will spill
        #hence, the shorter of the pair is the height of the water * length on the x-axis which is right - left
        area = min(nums[left], nums[right]) * (right - left)
        if area > max_qty:
            max_qty = area

        #if the left height is smaller then the only chance of getting a bigger quantity is to get a larger left height, so moving left pointer towards right by 1
        if nums[left] < nums[right]:
            left += 1
        #if the right height is smaller then the only chance of getting a bigger quantity is to get a larger right height, so moving right pointer towards left by 1
        elif nums[left] > nums[right]:
            right -= 1
        #if both heights are the same then if we move either one the length on x-axis will reduce but the height will remain the same or less, the quantity will never be more than the current value
        #hence, moving both pointers closer by 1
        else:
            left += 1
            right -= 1
    return max_qty

input = [2, 7, 8, 3, 7, 6]
print(find_larget_container(input))