from stack import Stack


def evaluate_postfix(expression, **kwargs):
    s = Stack()
    for token in expression:

        # remove whitespace
        token = token.strip()
        if token == '':
            continue
        # substitute and variables
        elif token in kwargs:
            s.push(kwargs[token])
        # push any single digit numbers
        elif token in "0123456789":
            s.push(float(token))
        # do the correct calculation
        elif not s.is_empty():
            plus = None
            if token == "+":
                plus = s.pop() + s.pop()
            elif token == "-":
                a = s.pop()
                b = s.pop()
                plus = b - a
            elif token == "*":
                plus = s.pop() * s.pop()
            elif token == "/":
                b = s.pop()
                a = s.pop()
                if b != 0:
                    plus = a / b
                else:
                    plus = 0
            if plus is not None:
                s.push(plus)

    return s.pop()


if __name__ == '__main__':
    print(evaluate_postfix("53-"))
    print(evaluate_postfix("53+"))
    print(evaluate_postfix("xx*x*25*/", x=10))
    print(evaluate_postfix("53*"))
