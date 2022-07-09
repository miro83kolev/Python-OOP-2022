class Student():
    def __init__(self, number, student_id):
        self.number = number # public by everyone
        self.__student_id = student_id # private encapsulated argument using 2 underscores in the star only in the class
        self._grades = [] # protected argument, only in class and inherits - only


student = Student('1234', '201010121')
print(student.number)
print(student._Student__student_id) # formula to access private attribute, mangling of the code