# def ss(nums):
#   n = len(nums)
#   for i in range(0,n):
#     min_index = i
#     for j in range(i+1,n):
#       if nums[j] < nums[min_index]:
#         min_index = j
#     nums[i],nums[min_index]=nums[min_index],nums[i]
#   return nums
# print(ss([1,222,3,44,5,66,7,88]))

# in descending order

def ss(nums):
  n = len(nums)
  for i in range(0,n):
    max_index = i
    for j in range(i+1,n):
      if nums[j]>nums[max_index]:
        max_index=j
    nums[i],nums[max_index]=nums[max_index],nums[i]
  return nums
print(ss([1,222,3,44,5,66,7,88]))

