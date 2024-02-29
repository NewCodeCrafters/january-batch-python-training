# dictionaries
names = ["Divine", "Spencer", "Kola", "Sunday"]
school = ["Light", "Front", "Lane", "Academy"]
age = [13, 12, 11, 12]
gender = ["Male", "Female", "Male", "Male"]

student1 = ["Divine", 13, "Light", "Male"]
student2 = ["Spencer", 12, "Front", "Female"]
student3 = ["Kola", 11, "Lane", "Male"]
student4 = ["Sunday", 12, "Academy", "Male"]

name = "Bola"
# combo of keys and values
# dictionaries can't be sliced or indexed
# They are also arbitrary
# keys are unique

students_bio = {
    # key: value
    "school": "LASUED",
    "names": ("Divine", "Spencer", "Kola", "Sunday"),
    "ages": [12, 13, 12, 11],
    "schools": ["Light", "Front", "Lane", "Academy"],
    "gender": ["Male", "Female", "Male", "Male"],
    # "ages": [12, 13, 11, 10]
}

engineers = {
    1: ["Mr. Ike", "Hardware Engineer"],
    5: ["Mr. Ike", "Hardware Engineer"],
    6: ["Mr. Ike", "Hardware Engineer"],
    7: ["Mr. Ike", "Hardware Engineer"],
    8: ["Mr. Ike", "Hardware Engineer"],
    2: ["Mr. Divine", "Machine Learning Engineer"],
    3: ["Mr. Spencer", "Cyber Analyst"],
    4: ["Mrs. Raji", "ML Developer"],
}

# print(type(students_bio["names"]))

print(engineers[2])

students_bio = {
    "A03/001": ["Taye", "Male", 19, "Art"],
    "A03/002": ["John", "Male", 18, "science"],
}
print(students_bio["A03/001"][1:3])