score = float(input("Enter your scores: "))
if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your grade is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is D")
elif score >= 0 and score < 60:
    print("Your grade is F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")
