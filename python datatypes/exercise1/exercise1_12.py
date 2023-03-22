#Write a program to find factorial of number 8

def factorial(n):
    k=1
    for i in range (0,n):
        k = k*(n-i)
    print(k)

factorial(8)


