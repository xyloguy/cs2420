from stack import Stack


def infix_to_postfix(expression):
    # set the precedence of the different operators
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    # create a stack to track the operators
    operator_stack = Stack()
    postfix = ''

    for token in expression:
        # skip whitespace characters
        token = token.strip()
        if token == '':
            continue
        # append operands to the postfix string
        elif token.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix += token
        # if the token is a left parentheses add it to the operator stack
        elif token == '(':
            operator_stack.push(token)
        # if the token is a right parentheses go through the
        # operator stack until the left parentheses is found
        # appending any operators to the postfix string
        elif token == ')':
            t = operator_stack.pop()
            while t != '(':
                postfix += t
                t = operator_stack.pop()
        # otherwise go through the operator stack (while there are operators left)
        # and if the next operator has a higher precedence than the current token "*/+-"
        # append it to the postfix string
        # lastly append the current token to the operator_stack
        else:
            while (not operator_stack.is_empty()) and (precedence[operator_stack.peek()] >= precedence[token]):
                postfix += operator_stack.pop()
            operator_stack.push(token)

    # finally after going through the entire expression append any operators left on
    # the stack to the postfix string.
    while not operator_stack.is_empty():
        postfix += operator_stack.pop()

    # return the postfix expression
    return postfix


if __name__ == '__main__':
    print(infix_to_postfix("x*7/(5-x)"))
