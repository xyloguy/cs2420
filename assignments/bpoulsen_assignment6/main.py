from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix

def get_user_expression():
    prompt = ''
    valid_chars = "x1234567890*/+-()"
    while prompt == '':
        user_prompt = input('Please enter an expression to graph. Valid characters include [{}]: '.format(valid_chars))
        user_prompt = user_prompt.lower()
        prompt = ''
        bad_input = False
        last_char_was_int = False
        for char in user_prompt:
            if char in valid_chars:
                if char in "1234567890":
                    if last_char_was_int:
                        print("Please only include single digit integers")
                        bad_input = True
                        break
                    else:
                        last_char_was_int = True
                else:
                    last_char_was_int = False
                prompt += char
            elif char.strip() == '':
                continue
            else:
                print('"{}" is not a valid character.'.format(char))
                bad_input = True
        if bad_input:
            prompt = ''
    return prompt


def main():
    while True:
        expression = get_user_expression()
        print(expression)
        postfix = infix_to_postfix(expression)
        print(postfix)
        x = None
        if 'x' in postfix:
            x = int(input('what is the value of x '))
        value = evaluate_postfix(postfix, x=x)
        print(value)


        x = input('Would like to graph another? [y/n]: ')
        if x.lower() == 'n':
            break


if __name__ == '__main__':
    main()
