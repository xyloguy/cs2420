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

    def __int__(self):
        return self.age

    def __float__(self):
        return float(self.__int__())


def read_names(students):
    print('READING NAMES')
    f = open('InsertNames.txt', 'r')
    t = 0
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
        t += 1
    end = time.time()

    print(t, 'records created.')
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def traverse_names(students):
    print('TRAVERSING NAMES')
    total = 0.0
    count = 0
    start = time.time()
    for student in students:
        total += int(student)
        count += 1
    avg_age = total / count
    end = time.time()
    print(count, 'records read')
    print('Average Age: {:04f}'.format(avg_age))
    print('Time: {:04f}'.format(end - start))
    print()


def delete_names(students):
    print('DELETING NAMES')
    f = open('DeleteNames.txt', 'r')
    t = 0
    start = time.time()
    for line in f:
        ssn = line.strip()
        deleted = False
        for i in range(len(students)):
            student = students[i]
            if student.ssn == ssn:
                del students[i]
                t += 1
                deleted = True
                break
        if deleted:
            continue
        print(ssn, 'not found')
    end = time.time()
    print(t, 'records deleted')
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def retrieve_names(students):
    print('RETRIEVING NAMES')
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
                total += int(student)
                count += 1
                break
        if found:
            continue
        print(ssn, 'not found')
    avg_age = total / count
    end = time.time()
    print(count, 'records retrieved')
    print('Average Age: {:04f}'.format(avg_age))
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def main():
    start = time.time()
    names = []
    read_names(names)
    traverse_names(names)
    delete_names(names)
    retrieve_names(names)
    end = time.time()
    print('Total Time: {:04f}'.format(end - start))


if __name__ == '__main__':
    main()
