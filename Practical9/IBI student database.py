class Student:
    def __init__(self, name, major, code_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_score = code_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        if int(self.code_score)>100 or int( self.group_project_score)>100 or int( self.exam_score)>100:
            print('error')
        else:
            print(f"Name: {self.name}, Major: {self.major}, Code Score: {self.code_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")

# example
student1 = Student("FLeix", "BMI", 100, 100, 100)
student1.print_details()
