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



def re( nums, val) :
        c=[]
        a=[]
        for i in range(len(nums)):
            if nums[i] != val:
                # num[]
                c.append(nums[i])
                a.append(nums[i])
        b=list(set(a))
        b.append(len(c))
        return b
a=re([3,2,2,3],3)
print(a)