import math
nums=[1,4,9,16,25]
res=tuple(math.sqrt(i) for i in nums)
print(res)


words=["madam","radar","abc"]
res=[i for i in words if i==i[::-1]]

print("palindrome strings are ",res)