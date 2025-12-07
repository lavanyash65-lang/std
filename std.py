def student_details(name, roll_no, course, marks):
    result = (
        f"Student Name: {name}\n"
        f"Roll Number: {roll_no}\n"
        f"Course: {course}\n"
        f"Marks: {marks}"
    )
    return result

if __name__ == "__main__":
    name = "Bob"
    roll_no = "R102"
    course = "BSc CS"
    marks = 87
    print(student_details(name, roll_no, course, marks))
