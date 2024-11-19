n = int(input("Enter the value of N: "))
a = 0
b = 1
count = 1
print(a,b, end=" ")
while(count < n-1):
    # with using a 3rd variable
    # c = a
    # a = b
    # b = b + c
    # without using a 3rd variable
    b = b + a
    a = b - a 
    print(b, end=" ")
    count += 1
#0 1 1 2 3 5 8 13 21 34 55 89