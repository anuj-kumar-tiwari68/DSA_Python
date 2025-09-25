# # try 1
# st = "malayalam"
# s = list(st)
# def pal(s,left,right):
#   if left>=right:
#     s[left],s[right]=s[right],s[left]
#     pal(s,left+1,right-1)
# pal(s,0,8)
# rev = ''.join(s)
# print(st==rev)

# # try 2
# def pal(s,left,right):
#   if left>=right:
#     return True 
#   if s[left]!=s[right]:
#     return False
#   return pal(s,left+1,right-1)
# pal("malayalam",0,len("malayalam"))

# with while loop
s = "malayalam"
n = len(s)
left = 0
right = len(s)-1
while left<right:
  if s[left]!=s[right]:
    print(False)
    break
  left+=1
  right-=1
else:
  print(True)

