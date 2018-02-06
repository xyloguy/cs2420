from stack import Stack


def evaluate_postfix(expression, **kwargs):
    s = Stack()
    for token in expression:
        plus = None

        token = token.strip()
        if token == '':
            continue
        elif token in kwargs:
            s.push(kwargs[token])
        elif token in "0123456789":
            s.push(int(token))
        elif not s.is_empty():
            if token == "+":
                plus = s.pop() + s.pop()
            elif token == "-":
                plus = s.pop() - s.pop()
            elif token == "*":
                plus = s.pop() * s.pop()
            elif token == "/":
                plus = s.pop() / s.pop()

        if plus is not None:
            s.push(plus)

    return s.pop()
