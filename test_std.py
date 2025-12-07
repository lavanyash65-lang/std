from std import student_details

def test_student_details():
    expected_output = (
        "Student Name: Bob\n"
        "Roll Number: R102\n"
        "Course: BSc CS\n"
        "Marks: 87"
    )
    assert student_details("Bob", "R102", "BSc CS", 87) == expected_output
