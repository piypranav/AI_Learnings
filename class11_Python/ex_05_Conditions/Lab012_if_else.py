age = int(
    input("Enter your age: ").strip()
)  # Convert input to integer and remove any leading/trailing whitespace

if age >= 18:
    print("You can drive a car.")
else:
    print("You cannot drive a car.")


print("you can drive a car" if age >= 18 else "you cannot drive a car")
