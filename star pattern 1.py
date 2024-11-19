#       *
#    *  *  *
# *  *  *  *  *

#   *
#  ***
# *****
n = int(input("Enter number of rows: "))
n+=1
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*"*(i*2-1),end="")
    print()