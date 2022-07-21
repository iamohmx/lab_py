# size = int(input())

# if size<=34:
#     print("xs")
# elif size<=36:
#     print("s")
# elif size<=38:
#     print("m")
# elif size<=40:
#     print("l")
# elif size>=40:
#     print("xl")
# else:
#     print("กรุณาติดต่อร้านค้


# i = 10


# for i in range(10, 0, -1):
#         print(i)
        

# for i in range(10, 0, 1):
#     print(i)




# a = "Hello"

# print("%s" % a)

# a = 5

# print("a is %.2f" % a)


# num1 = int(input())
# num2 = int(input())

# result = num1 + num2
# print("%d + %d = %d " % (num1,num2,result))

# result = num1 - num2
# print("%d - %d = %d " % (num1,num2,result))

# result = num1 * num2
# print("%d * %d = %d " % (num1,num2,result))

# result = num1 / num2
# print("%d / %d = %d " % (num1,num2,result))


# num1 = int(input())
# num2 = int(input())


# if(num1 > num2):
#     print("A")
# elif(num1 == num2):
#     print("AB")
# else:
#     if(num1 < num2):
#         print("B")



# print("*\n**\n***\n****\n*****\n******")
# print("    $")
# print("   $ $")
# print("  $ $ $")
# print(" $ $ $ $")
# print("$ $ $ $ $")



# name = input()
# year = int(input())
# year = 2020-year
# if (year >=  18):
#     print("Welcome %s To NongGipsy Pub" % name)
# else:
#     print("You shall not pass!")



# from tkinter.tix import MAX


# num1 = int(input())
# num2 = int(input())

# print("MAX : ",max(num1,num2))
# print("MIN : ",min(num1,num2))

# string = input()
# spa = string.split()
# spa = list(reversed(spa))
# print(" ".join(spa))



# num = int(input())

# for i in range(num):
#     print("")
#     for j in range(i):
#         print("* " ,end=" ")
        


# 
 
# Function to demonstrate printing pattern triangle
# def triangle(n):
     
#     # number of spaces
#     k = n - 1
 
#     # outer loop to handle number of rows
#     for i in range(0, n):
     
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end="")
     
#         # decrementing k after each loop
#         k = k - 1
     
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
         
#             # printing stars
#             print("*", end="")
     
#         # ending line after each row
#         print("\r")
 
# # Driver Code
# n = int(input())
# triangle(n)


# โปรแกรมคำนวณกำไร
# cost = float(input("Cost: "))
# profit = int(input("Profit: "))
# cal = cost / (100 - profit) * 100
# print("You Should Sell  %.2f baht" % cal)


# num = int(input())

# if num >= 0:
#     print("Even")
# else:
#     print("Odd")


# i = []
# for i in range(1,num+1):
#     print(i)
# find = int(input())
# if i != find:
#     print("No")
# else:
#     print("Yes")
# 
# 
# num = int(input())

# if num % 3 == 0 and num % 2 == 0:
#     print("fizzbuzz")
# elif num % 3 == 0:
#     print("fizz")
# elif num % 2 == 0:
#     print("buzz")


fname = input()
lname = input()
addr = input()
gender = input()
tel = input()

print("--- Customer Detail ---")
print("Name : %s %s" % (fname, lname))
print("Address : %s" % (addr))
print("Gender : %s" % (gender))
print("Tel : %s" % (tel))