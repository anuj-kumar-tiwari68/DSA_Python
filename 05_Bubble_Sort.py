def bs(num):
  n = len(num)
  is_Swap = False
  for i in range(n-2,-1,-1):
    # max_val = i
    for j in range(0,i+1):  
      if num[j]>num[j+1]:
      
        num[j],num[j+1]=num[j+1],num[j]
        is_Swap = True
    if is_Swap == False:
      break

lst = [1,222,3,44,5,66,7,88]
bs(lst)
print(lst)