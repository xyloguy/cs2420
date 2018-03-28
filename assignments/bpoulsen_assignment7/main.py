import time
from student import Student
from bst import BST


def read_names(students):
    print('READING NAMES')
    f = open('InsertNames.txt', 'r')
    t = 0
    start = time.time()
    for line in f:
        last, first, ssn, email, age = line.split()
        s = Student(last, first, ssn, email, age)
        skip = False

        student = students.find(s)
        if student:
            print('Could not add:', s, '-> Duplicate:', student.val, 'already exists')
            continue

        students.insert(s)
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
        student = students.find(ssn)
        if student != False:
            student.delete(ssn)
            t += 1
            continue
        print(ssn, 'not found')
    end = time.time()
    print(t, 'records deleted')
    print('Time: {:04f}'.format(end - start))
    f.close()
    print()


def main():
    students = BST()
    read_names(students)
    #traverse_names(students)
    delete_names(students)


if __name__ == '__main__':
    main()