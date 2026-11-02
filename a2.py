#1

# n= int(input("enter no: "))

# table=[]
# for i in range(1,11):
#     table.append(n*i)

# table =[n*i for i in range(1,11)]

   #2 
# with open("table.txt", "a") as p:
#     p.write("\n"+"table of " + str(n) + ": " + str(table) + "\n")

# a= "{} is a good {}".format("rohit","boy")
# print(a)
# b= "{} is a good {}".format("rohit","boy")
# print(b)
  

# 3
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_worLD():
#    return 'Hello LOOOOOOOOSEER'

# if __name__ == '__main__':
#    app.run()


# # 4
# s= "hello bro back to ground"
# l= list(s.split())
# print(s.split())
# print(len(l[-1]))
# print(l[-1])
# print(s.split())
# # print(l)

# def le(s):             
#         end = len(s) - 1
#         print("end",end)
#         while s[end] == " ":
#             end -= 1
#             print("and",end)
#         print("e",end)
#         start = end
#         while start >= 0 and s[start] != " ":
#             start -= 1
#             print("s",start)
#         return end - start
# print(le("helo"))



# def re( nums, val) :
#         c=[]
#         a=[]
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 # num[]
#                 c.append(nums[i])
#                 a.append(nums[i])
#         b=list(set(a))
#         b.append(len(c))
#         return b
# a=re([3,2,2,3],3)
# print(a)

# nums = [0,1,0,3,12]


# def cal(operations) :
#         i=0
#         l=[]
#         for j in range(len( operations)) :
#             if operations[j] == "C":
#                 l.pop(-1)
#             elif operations[j] == "D":
#                 l.append(l[-1]*2)
#             elif operations[j]== "+" :
#                 a = l[-1]+l[-2]
#                 l.append(a)
#             else: 
#                 l.append(int(operations[j]))
#             print(l)
#         for e in l :
#             i = i+ int(e)

#         return i
# print(cal(["5","2","C","D","+"])) 


# def maxArea( height) :
#        ma = height[0] 
#        for i in range(len(height)) :
#             if ma > height[i] and height[i] != max(height) : 
#                 ma = height[i]
#                #  print(ma)

#        print(ma)
#        print(max(height)) 
#        return ma*(height.index(max(height))-height.index(ma)) 
# print(maxArea([1,8,6,2,5,4,8,3,7]))
 
# def m( nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
      #   l= []
      #   b=[]
      #   for i in range(len(nums1)):
      #       a = nums1[i]-nums2[i]
      #       if a <0 :
      #          a = a-2*(a)
      #       l.append(a)
      #   for i in range(k1):
      #       # while (i<k1) :
      #           # b = [max(l)-1 for x in l]
      #           b.append(max(l)-1)
      #           l.remove(max(l))
      #           l.append(max(l)-1)
      # #   l.extend(b)
      #   print("l", l)
      #   b.clear()
      #   for i in range(k2):
      #       # while (i<k1) :
      #           # b = [max(l)-1 for x in l]
      #           b.append(max(l)-1)
      #           l.remove(max(l))
      #           l.append(max(l)-1)
      # #   l.extend(b)
      #   print("l", l)
      #   return sum([x**2 for x in l])
#         l= []    
#         c = len(nums1)
#         for i in range(c):
#             a = nums1[i]-nums2[i]
#             if a <0 :
#                a = a-2*(a)
#             l.append((a))
#         print("l",l) 
#         for i in range(k1):
#                 y=max(l)
#                 if y == 0 :
#                     break   
#                 ind = l.index(y)
#                 l[ind] = y-1
#         print("l",l)    
#         for i in range(k2):
#                 z=max(l)
#                 if z==0:
#                   break
#                 ind = l.index(z)
#                 l[ind] = z-1
#         print("l",l)    

#         return sum([x**2 for x in l])
# print(m([10,10,10,11,5],[1,0,6,6,1],11,27))
# print(m([1,4,10,12],[5,8,6,9],10,5))


# a = [1,2,3]
# print((a))
# print(a[:2])

# def f( nums: list[int]) -> list[int]:
#         i=0
#         j=len(nums)
#         n= []
#         p=1
#         def pn(a):
#             prod=1
#             if len(a)==1:
#                 return a[0]
#             for i in range(1,len(a)+1):
#                 prod=i*pn(a-1)  

#             return prod
#         for x in range(j) :
#           if x==0:
#                 p = pn(nums[1:])
#           else:        
#             p= pn(nums[:x])* pn(nums[x+1:])
#           n.append(p)
#         return n
# print(f([1,2,3,4]))


# def f(nums: list[int]) -> list[int]:
#     n = []
#     for x in range(len(nums)):
#       p = 1
#       for y in range(len(nums)):
#         if x == y:
#           continue
#         p *= nums[y]
#       n.append(p)        
#     return n
# def f( nums: list[str], k: int) -> str:
#         a=[]
#         for i in nums:
#             a.append(int(i))
            
#         print(a)
#         n2=sorted(a)
#         a = n2[len(nums)-k]
#         return str(a)
        
# print(f(["3","6","7","10"],4))  # Output: [24, 12, 8, 6]




def rotate(nums: list[int], k: int) -> None:
    a=[]
    for i in range(k):
        a.append(nums[-k])
        print("a",a)
        nums.pop(-k)
        k-=1
        # print(a)
        # nums.insert(0,a[0])
        # a.pop(-1)
    print(a)
    # nums= a+nums
    nums[:0]=a
    return nums
print(rotate([1,2,3,4,5,6,7],3))