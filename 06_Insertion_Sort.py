def Is(nums):
  n = len(nums)
  for i in range(1,n):
    key=nums[i]
    j = i-1
    while j >= 0 and nums[j]>key:
      nums[j+1]=nums[j]
      j-=1

    nums[j+1]=key
lst = [1,222,3,44,5,66,7,88]
Is(lst)
print(lst)