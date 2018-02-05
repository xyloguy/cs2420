import time


class Student:
    def __init__(self, last, first, ssn, email, age):
        self.last = last
        self.first = first
        self.ssn = ssn
        self.email = email
        self.age = int(age)

    def __str__(self):
        return '{} - {} {}'.format(self.ssn, self.first, self.last)

    def __eq__(self, other):
        return self.ssn == other.ssn


def read_names(students):
    print('Reading Names')
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
    print('Total time: {:06f}'.format(end - start))
    f.close()


def traverse_names(students):
    print('Traversing Names')
    total = 0.0
    count = 0
    start = time.time()
    for student in students:
        total += student.age
        count += 1
    avg_age = total/count
    end = time.time()
    print('Average Age: {:06f}'.format(avg_age))
    print('Total time: {:06f}'.format(end - start))


def delete_names(students):
    print('Deleting Names')
    f = open('DeleteNames.txt', 'r')
    start = time.time()
    for line in f:
        ssn = line.strip()
        deleted = False
        for i in range(len(students)):
            student = students[i]
            if student.ssn == ssn:
                del students[i]
                deleted = True
                break
        if deleted:
            continue
        print(ssn, 'not found')
    end = time.time()
    print('Total time: {:06f}'.format(end - start))
    f.close()


def retrieve_names(students):
    print('Retrieving Names')
    f = open('RetrieveNames.txt', 'r')
    total = 0.0
    count = 0
    start = time.time()
    for line in f:
        ssn = line.strip()
        found = False
        for student in students:
            if student.ssn == ssn:
                found = True
                total += student.age
                count += 1
                break
        if found:
            continue
        print(ssn, 'not found')
    avg_age = total / count
    end = time.time()
    print('Average Age: {:06f}'.format(avg_age))
    print('Total time: {:06f}'.format(end - start))
    f.close()


if __name__ == '__main__':
    names = []
    read_names(names)
    traverse_names(names)
    delete_names(names)
    retrieve_names(names)
