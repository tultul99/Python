#Class method construct

class student:
    roll = ""
    gpa = ""

    def setValue(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa 

    def display (self):   # method
        print(f'Roll : {self.roll}, GPA : {self.gpa}')


asme = student()   # object
print(isinstance(asme,student))

# asme.gpa = 3.9
# asme.roll = 3882
asme.setValue(3882, 3.9)
# print(f'Roll : {asme.roll}, GPA : {asme.gpa}')
asme.display()

shanto = student()
shanto.gpa = 3.9
shanto.roll = 3871
print(f'Roll : {shanto.roll}, GPA : {shanto.gpa}')


class queen:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):   # constructor, special method
        self.roll = roll
        self.gpa = gpa

    def display (self):   # method
        print(f'Roll : {self.roll}, GPA : {self.gpa}')

naher = queen(1234,4.0)
naher.display()
