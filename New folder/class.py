class student:
    def __init__(self, name, rollno, marks):
        self.name = "Anubhav"
        self.age = 20
        self.marks = 90

    def talk(self):
        print("hello ", self.name)
        print("My age is ", self.age)
        print("My Marks are ", self.marks)


s = student("Anubhav", 66, 89)
s.talk()
