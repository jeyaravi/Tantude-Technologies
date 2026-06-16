num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10
    count += 1
    num //= 10
print("The count of the digits is:", count)