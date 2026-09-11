n = int(input("Please Enter The Number Of Fibonacci Terms:"))
a,b=0,1

for i in range(n):
    print(a,end=" ")
    a,b =b,a+b