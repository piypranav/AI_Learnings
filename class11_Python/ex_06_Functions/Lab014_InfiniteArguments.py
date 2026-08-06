def print_infinite_arg(*args):
    for i in args:
        print(i)


print_infinite_arg(1, 2, 3, 4, 5)
print_infinite_arg("piyush")
print_infinite_arg("piyush", "pranav")
print_infinite_arg("piyush", "pranav", "piy.pranav@gmail.com")
print_infinite_arg("1", "piyush", "pranav", "piy.pranav@gmail.com", True, 3.14)
