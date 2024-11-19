n = int(input("Enter a positive number: "))
def prime(num):
    count = 0
    if num == 1 or num == 2:
        return "Not prime Number"
    if num > 1:
        for i in range(1, num):
            if num % i == 0:
                count += 1
        if count == 0:
            return "Prime Number"
        return "Not a prime number"
print(prime(n))