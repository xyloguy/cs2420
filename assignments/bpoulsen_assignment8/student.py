class Student:
    def __init__(self, last, first, ssn, email, age):
        self.last = last
        self.first = first
        self.ssn = ssn
        self.email = email
        self.age = float(age)

    def __int__(self):
        return int(self.ssn.replace('-', ''))

    def __float__(self):
        return float(self.age)
