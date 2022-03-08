n = int(input("Enter the number of student: "))

student = {}

for i in range(n):
    studentindex = i+1

    student[studentindex] = {}

    RollNo = int(input("Enter the roll number of student: "))
    Name = input("Enter the name of student: ")
    Marks = int(input("Enter the Marks: "))

    grade = None
    if(90 < Marks <= 100):
        grade = "A"
    elif(80 < Marks <= 90):
        grade = "B"
    elif(60 < Marks <= 80):
        grade = "C"
    elif(40 < Marks <= 60):
        grade = "D"
    elif(0 < Marks <= 40):
        grade = "Fail"
    else:
        grade = "Invalid"

    student[studentindex]["RollNo"] = RollNo
    student[studentindex]["Name"] = Name
    student[studentindex]["Marks"] = Marks
    student[studentindex]["grade"] = grade

print(student)