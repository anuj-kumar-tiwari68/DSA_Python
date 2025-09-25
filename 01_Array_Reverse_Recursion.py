# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def rev(nums,left,right):
#   if left>=right:
#     return
#   nums[left],nums[right]=nums[right],nums[left]
#   rev(nums,left+1,right-1)
# rev(nums,2,5)
# print(nums)


import numpy as np
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = np.array(n)
left = 0
right = len(nums)-1
while left <= right:
  nums[left],nums[right]=nums[right],nums[left]
  left+=1
  right-=1
print(nums)
