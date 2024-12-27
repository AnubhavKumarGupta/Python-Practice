class anubhav:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

m1 = anubhav(100)
m2 = anubhav(150)

print(m1 + m2)
