class Student:
    def __init__(self, last, first, ssn, email, age):
        self.last = last
        self.first = first
        self.ssn = ssn
        self.email = email
        self.age = int(age)

    @property
    def key(self):
        return self.ssn

    def __str__(self):
        return '{} {} {}'.format(self.ssn, self.first, self.last)

    def __lt__(self, other):
        if isinstance(other, str):
            return self.key < other
        return self.key < other.key

    def __eq__(self, other):
        if isinstance(other, str):
            return not self.key < other and not other < self.key
        return not self.key < other.key and not other.key < self.key

    def __int__(self):
        return self.age

    def __float__(self):
        return float(self.age)