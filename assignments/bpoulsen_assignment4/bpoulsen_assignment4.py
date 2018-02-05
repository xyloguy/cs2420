import time


class Student:
    def __init__(self, last, first, ssn, email, age):
        self.last = last
        self.first = first
        self.ssn = ssn
        self.email = email
        self.age = int(age)

    def __str__(self):
        return '{} {} {}'.format(self.ssn, self.first, self.last)

    def __eq__(self, other):
        return self.ssn == other.ssn


def read_names(students):
    f = open('InsertNames.txt', 'r')
    start = time.time()
    for line in f:
        last, first, ssn, email, age = line.split()
        s = Student(last, first, ssn, email, age)
        skip = False
        for student in students:
            if student == s:
                print('Could not add:', s, '-> Duplicate:', student, 'already exists')
                skip = True
                break
        if skip:
            continue
        students.append(s)
    end = time.time()
    print('Total time: {:04f}'.format(end - start))
    f.close()


if __name__ == '__main__':
    names = []
    read_names(names)

