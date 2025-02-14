# Full name : Odiljon G'ulomov
# Student ID : 230234
# Department : SED 1
# Course name : Introduction to Data Science
# Contest 1
# Solved and uploaded in 14th February 2025

from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

if __name__ == "__main__":
    decorator_1(kwargsAcceptFun)(
        fullName = "Odiljon Gulomov",
        studying_at_university = True,
        university_name = "New Uzbekistan University",
    )
    
    transformed_data = decorator_1(typeBasedTransformer)(
        integer_value=5,
        float_value=3.14,
        name="Odil",
        boolean_value=True,
        numbers=[90, 80, 70],
        course_info={"year": 2025, "course":"Intro to Data Science"},
        unsupported_type={1, 2, 3}
    )
    print("\nTransformed Data:", transformed_data)

