n = int(input("Enter a number: "))
n+=1
for i in range(n):
    print(" "*(n-1-i), end="")
    print("*"*i, end="\n")
 