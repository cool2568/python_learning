# # TWO SUM
# nums=[2,7,11,15]
# target=9
# blanck=[]
# total=0
# for i in range(len(nums)):
#     for j in range(len(i+1,nums)):
#         if nums[i]+nums[j]==target:
#             result=[i,j]
#     break


# seen={}

# for num,value in enumerate(nums):
#     diff=target-value
#     if diff in seen:
#         print(seen[diff],num)
#     break
# seen[value]=num


# Valid anagram 
# s="rat"
# t="car"
# l1=[]
# l2=[]
# for i in s:
#     l1.append(i)
#     print(l1)
# for l in t:
#     l2.append(l)
#     print(l2)
# if l1 in l2:
#     print(True)
# else:False


# Valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        # 1. Fill the ledger (Loop 1)
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # 2. Audit the ledger (Loop 2 - Must be OUTSIDE Loop 1)
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
                
        return True

# contains duplicate
nums=[1,2,3,1,4,4]
count={}

for num in nums:
    if num in count:
        print(True)
    else:
        count[num]=True
    
# best time to buy a stock
prices = [7,1,5,3,6,4]



