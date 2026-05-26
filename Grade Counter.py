# Grade Counter
import csv
import os
path = os.path.join(os.path.dirname(__file__), "Students.csv")

def Student_Input():
     done = False
     
     while not done:
        Student_Name_Input = input("Input student name or skip : ")
        if Student_Name_Input == "skip":
            break
        Student_Grade_Input = int(input("Input student grade : "))
        with open(path, "a", newline="") as Input_Students:
            Fields = ["Name", "Grade"]
            write = csv.DictWriter(Input_Students, fieldnames=Fields)
            write.writerow({"Name" : Student_Name_Input, "Grade" : Student_Grade_Input})

        while True:
            Again = input("Try again? (Y/N) : ")
            if Again.lower() == "y":
                break
            elif Again.lower() == "n":
                done = True
                break
            else:
                print("Try again")
            

def Remove_Student():
    New_Student_List = []
    with open(path, "r") as Student_Info:
        read = csv.DictReader(Student_Info)
        for index, student in enumerate(read):
            print(f"{index + 1} | Name : {student["Name"]} - Grade : {student["Grade"]}")
            New_Student_List.append(student)

        while True:
            try:
                Remove_Input = int(input("Remove a specific student by number : "))
                if 1 <= Remove_Input <= len(New_Student_List):
                    New_Student_List.pop(Remove_Input - 1)
                    break
                else:
                     print("Number not found")
            except ValueError: 
                print("Only numbers!")

    with open(path, "w", newline="") as New_Students:
        fields = ["Name", "Grade"]
        write = csv.DictWriter(New_Students, fieldnames=fields)
        write.writeheader()
        write.writerows(New_Student_List)


def Grades():
    Students_List = []
    with open(path, "r") as Student_Info:
        read = csv.DictReader(Student_Info)
        for student in read:
            Students_List.append(student)

    if not Students_List:
         print("There are no students")
    else:
        for student in Students_List:
            if int(student["Grade"]) >= 90:
                        print(f"{student["Name"]} gets an A ({int(student["Grade"])})")
            elif int(student["Grade"]) >= 80:
                        print(f"{student["Name"]} gets a B ({int(student["Grade"])})")
            elif int(student["Grade"]) >= 70:
                        print(f"{student["Name"]} gets a C ({int(student["Grade"])})")
            else:
                        print(f"{student["Name"]} gets a D ({int(student["Grade"])})")

Student_Input()
Grades()

while True:
    Options = input("Input New | Remove | Show Grades : ")
    if Options.lower() == "input new":
        Student_Input()
    elif Options.lower() == "remove":
        Remove_Student()
    elif Options.lower() == "show grades":
        Grades()
    else:
         print("Try again")


