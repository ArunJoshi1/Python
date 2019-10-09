class Student:
    def __init__(self, fname, lname, roll, sem):
        self.fname = fname
        self.lname = lname
        self.roll = roll
        self.sem = sem

    def printStudent(self):
        return f'{self.fname} {self.lname} roll number {self.roll} {self.sem}semester \nemail-> {self.email}'

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    @property
    def fullName(self):
        return f'{self.fname} {self.lname}'

    @fullName.setter
    def fullName(self, name):
        fname, lname,_ = name.split(' ')
        self.fname = fname
        self.lname = lname


student = Student('arun', 'joshi', 1627998, '7th')
student.fullName='sham lal thaluh'

print(student.printStudent(), "\nfull name " + student.fullName)
