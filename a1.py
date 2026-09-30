# def a():
#     return"helo"
# #     print("hello ANTIGRAVITY")
# # print(a())


# # hello = None
# # print("helloG",end="")
# # print(35,"hello",hello, sep="-")
# # print("35"+"hello"+hello)   # error

# def re(l,w):
#     n=[]
#     for i in l:
#         if w not in i:

#             n.append(i.strip(w))#removes "sh" from the list if "sh" is at the starting or end
#     return n
# l=["harry","ansh","ashish", "abhay"]
# print(re(l,"sh"))
# print(l.index("ashish"))

# # number = "123-45 6"

# # def r( head, val):
# def l(s):
#     # c=""
#     # for i in range(len(s)):
#     #     if s[i] in s[i+1:]:
#     #         print()
#     #         c+=s[i] 
#     #         print(s[i])
#     #     # return True
#     #     class Solution:
#     # def lengthOfLongestSubstring(self, s: str) -> int:
#         char_index = {}
#         max_length = 0
#         left = 0
#         for right in range(len(s)):
#             # Agar character duplicate hai aur window mein hai
#             if s[right] in char_index and char_index[s[right]] >= left:
#                 left = char_index[s[right]] + 1
#                 print("l1    ",left)
#             # Current character ka index store kar
#             char_index[s[right]] = right
#             print(char_index)
#             # Max length update kar
#             max_length = max(max_length, right - left + 1)
#             print("m    ",max_length)
#         return max_length
# s = "abcabcbb"
# a=l(s)
# print(a)

# """a="anshg"
# print(a)
# # b= '''ans'''

# h"""
# print(b)
# """anshtya"""'''
# print(c)'''


# def r(num):
#         a= nums.copy()
#         # nums.remove(nums[1])
#         print("a = ",a)
#         n= len(a)
#         for i in range(1,n):
#             if a[i]==a[i-1]:
#                 nums.remove(a[i])
#                 print("nums:   ",nums)
#         return len(nums)

# nums=[0,0,1]
# p=r(nums)
# print(p)



# print(5/2)
# print(5//2)

# import sys 
# print(sys.version)
# def f(n):
#     if(n>=1):
#      print(2*n,end=" ")
#      f(n-1)
#         # return 1
#     # else:
# f(15)


# def l(digits):
#         a ="".join(map(str,digits))
#         b= int(a) + 1
#         # b=str(b)
#         c=list(str(b))
#         return [int(i) for i in c]   # to convert string list to int list
# a =list([1,2,3])
# print(l(a))
# n=10
# for i in range(n - 1, 0 -1):
#     print(i)


def t(prices):
        # max=0
        # low = 0
        # maxi=0
        # if len(prices)<2:
        #     return 0
        # else:
        #  if max-low > maxi:
        #         maxi = max-low
        #  else :
        #   low = prices[0]
        #   for i in range(1,len(prices)) :
        #     if low >= prices[i]:
        #         low = prices[i]
        #         print(low," : low")
           
            #     for j in range(i, len(prices)):

            #         if max < prices[j]:
            #             max=prices[j]
            #             print(max , " :max")
            # elif(prices[i-1]<= prices[i]) and low <= prices[i]:
            #     for j in range(i, len(prices)):

            #         if max <= prices[j]:
            #             max=prices[j]
            #             print(max , " :max")
            # else:
            #     low = 0
            # print(low," :low")
            # if maxi < max-low:
            #     maxi = max-low
            # else:
            #     return 0
            # return maxi
        profit =0 
        # low = float('inf')
        low = prices[0]
        for i in range(0,len(prices)):
            if low > prices[i] :
                low = prices[i]
            # else :
            elif profit < prices[i] -low :
                    profit = prices[i] -low
                # else :
                #     continue 
            
        return profit

print(t([2,1,2,1,0,1,2]))
# print(t([7,1,5,3,6,4]))
# prices =
# [2,1,2,1,0,1,2]