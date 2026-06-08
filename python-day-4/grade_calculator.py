name = input("Student Name: ")
marks = int(input("Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Student Name:", name)
print("Grade:", grade)

