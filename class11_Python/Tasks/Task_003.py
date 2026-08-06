def sum1(*args):
    total = 0
    for num in args:
        total = total + num

    return total


def sum(num1=100, num2=200, num3=300):
    return num1 + num2 + num3


print("Sum of 10, 20, 30 is: ", sum(10, 20, 30))
print("Sum of 100, 200, 300, 400, 500 is: ", sum1(100, 200, 300, 400, 500))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("Sum of", num1,",", num2, "and", num3, "is: ", sum(num1, num2, num3))
