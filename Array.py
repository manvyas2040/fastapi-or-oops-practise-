# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[9,8,7],[6,5,4],[3,2,1]]
# result=[[0,0,0],[0,0,0],[0,0,0]]

# for row in a :
#     print(row)

# print(a[1][2])
# for i in range (len(a)):
#     for j in range(len(a[0])):
#         print(a[i][j],end=" ")
#     print()
# for i in range (len(b)):
#     for j in range(len(b[0])):
#        result[i][j]=a[i][j]+b[i][j]
# for row in result:
#     print(row)

# rows=int(input("enter rows :"))
# cols=int(input("enter cols :"))
# matrix=[]
# print("enter matrix values row-wise :")
# for i in range(rows):
#   row=list(map(int,input().split()))
#   matrix.append(row)

#   for i in matrix:
#     print(matrix)

# total=0
# for row in matrix :
#     for val in row:
#         total += val
# print("total :",total)

# for row in matrix:
#     for val in row:
#         print(f"{val:3}",end="")
#     print()

# a=[1,2,3,4,5,6,7,8,9,10]
# for n in a:
#     if n %2==0:
#         print(n)

# array=[]
# for i in range(5):
#     num=int(input("enter a num :"))
#     array.append(num)
# print("array:",array)
# print("sum :",sum(array))

# array=[20,23,40,50,60]

# array.pop(2)
# print("after pop",array)

# array.remove(20)
# print("after remove :",array)


# rows=int(input("enter a rows value : "))
# cols=int(input("enter a cols value :"))
# matrix=[]

# print("enter matrix value row-wise : ")

# for i in range(rows):
#     row=list(map(int,input().split()))
#     matrix.append(row)
#     for i in matrix:
#         print(matrix)

########### list  ##########

# a=[1,2,3,4,5,6,7,8,9,13,17,19,]
# lar=a[0]
# index=0
# for i in range(len(a)):
#     if a[i] > lar:
#         lar=a[i]
#         index=i

# print(f"the largest number is{lar} and index is {index} ")



# a=[2,326,59,45,12]
# sum =0

# for i in a:
#     sum +=i
# print(sum/len(a))

# a=[2,326,59,45,12,68,100,500]
# sec_largest=a[0]
# largest=a[0]

# for i in a:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest,largest)

# a=[1,2,3,4,5,6]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your lis is not sorted ")
#         break
# else:
    # print("your list is sorted ")

########## dis ###########3

# a={10:100,20:200,30:300,40:400}
# b={100:1000,200:2000,300:3000,400:4000}
# sum = 0
# a[10]=1000
# a[50]=500
# del a[30]

# print(a)
# for i in a :  # for values : for i in a.values():
#     print(i)   # or print(a[i])

# print(a.items())
# for i in b:
#     a[i] = b[i]
# print(a)

# for i in a:
#     sum += a[i]
# print(sum)

# a=[1,1,1,1,1,1,1,2,2,2,3,3,3,4,4,5,5,5,5,5]

# d={}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# a={10:100,20:200,30:300,40:400}
# b={40:500,60:600,70:700,80:800}

# for i in b:
#     if i in a.keys():
#         a[i] = b [i]
#     else:
#         a[i] = b[i]
# print(a)


 ########  exception handling #####
# a=int(input("enter a number: "))
# try:
#     print(10/a)
# except Exception as error:  # all error show
#     print(f"sorry you have an error by {error} ")
# else:
#     print("good work not any error !!")
# finally:
#     print("I always run....")

# age =int(input("enter a your age : "))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age is must be betwen 10 and 18")
#     else:
#         print("welcom your school ")
# except Exception as error:
#     print(f"error is ocerd by {error}")

############# file handling  #########

A=open("code.txt",'x')
A=open("code.txt",'w')
A.write("pythone topic\n")
A.write("pythone intro\n")
A.write("pythone parctis set\n")
print("file writed!!")

A=open("code.txt",'r')
print(A.read())