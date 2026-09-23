# q11
# n=12345
# x=0
# while(n!=0):
#     y=n%10
#     x=x*10+y
#     n=n//10
# print("reverse:",x)


# q12
# n=int(input("enter a number to check:"))
# original=n
# x=0
# while(n!=0):
#     y=n%10
#     x=x*10+y
#     n=n//10
# if(original==x):
#     print("the given no is palindrome")
# else:
#     print("the given no is not a palindrome")
# q13
# n = int(input("Enter a number: "))

# i = 2
# while i < n:
#     if n % i == 0:
#         print("Not Prime")
#         break
#     i += 1
# else:
#     if n > 1:
#         print("Prime")
#     else:
#         print("Not Prime")
# q14
n = int(input("Enter a number: "))

i = 2

while i <= n:
    j = 2

    while j<i:
        if(i%j!=0):
            print(j) 
            j+= 1 

    i += 1
       

  


