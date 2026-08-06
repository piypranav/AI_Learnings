def greetings():
    print("Hello, World!")


def greet(name):
    print("Hello ", name)


greetings()
greet("Alice")
greet("Bob")


def sum(a, b=15):  # default value of b is 15
    return a + b


sum_result = sum(5, 10)
print("Sum:", sum_result)

sum_result = sum(5)
print("Sum:", sum_result)


# Multiple return values (Only possible in Python)
def calculate(a, b=20):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result


calculate_result = calculate(10, 5)
print("Calculate:", calculate_result)

calculate_result = calculate(2)
print("Calculate:", calculate_result)


def sum_of_two_nums(num1=3, num2=5):
    return num1 + num2


sum_result = sum_of_two_nums()
print("Sum:", sum_result)

sum_result = sum_of_two_nums(20, 30)
print("Sum:", sum_result)
