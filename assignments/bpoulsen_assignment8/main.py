import time
from student import Student
from hashtable import HashTable


def read_names(students, size):
    print('READING NAMES')
    f = open('InsertNames{}.txt'.format(size), 'r')
    t = 0
    dups = 0
    start = time.time()
    for line in f:
        last, first, ssn, email, age = line.split()
        s = Student(last, first, ssn, email, age)
        student = students.retrieve(s)
        if student is None:
            students.insert(s)
            t += 1
        else:
            dups += 1
    end = time.time()

    print(t, 'records created.')
    print(dups, 'duplicates found.')
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def traverse_names(students, size):
    print('TRAVERSING NAMES')
    total = 0.0
    count = 0
    start = time.time()
    for student in students:
        total += float(student)
        count += 1
    avg_age = 0
    if count != 0:
        avg_age = total / count
    end = time.time()
    print(count, 'records read')
    print('Average Age: {:04f}'.format(avg_age))
    print('Time: {:04f}'.format(end - start))
    print()


def delete_names(students, size):
    print('DELETING NAMES')
    f = open('DeleteNames{}.txt'.format(size), 'r')
    t = 0
    err = 0
    start = time.time()
    for line in f:
        ssn = line.strip()
        s = Student('', '', ssn, '', 0)
        if students.delete(s):
            t += 1
            continue
        else:
            err += 1
    end = time.time()
    print(t, 'records deleted')
    print(err, 'records not found')
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def retrieve_names(students, size):
    print('RETRIEVING NAMES')
    f = open('RetrieveNames{}.txt'.format(size), 'r')
    total = 0.0
    count = 0
    err = 0
    start = time.time()
    for line in f:
        ssn = line.strip()
        s = Student('', '', ssn, '', 0)
        found = False
        student = students.retrieve(s)
        if student is not None:
            found = True
            total += float(student)
            count += 1
        if not found:
            err += 1
            continue
    avg_age = total / count
    end = time.time()
    print(count, 'records retrieved')
    print(err, 'records not found')
    print('Average Age: {:04f}'.format(avg_age))
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def main():
    size = ''

    s = 30000
    if size == 'Medium':
        s = 300000
    elif size == 'Big':
        s = 3000000
    else:
        size = ''

    start = time.time()
    students = HashTable(s)
    read_names(students, size)
    traverse_names(students, size)
    delete_names(students, size)
    retrieve_names(students, size)
    end = time.time()
    print('Total Time: {:04f}'.format(end - start))


if __name__ == '__main__':
    main()
