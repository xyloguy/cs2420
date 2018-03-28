import pygame
from evaluate_postfix import evaluate_postfix
from infix_to_postfix import infix_to_postfix


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


def draw_graph(surface, width, height, scale):
    surface.fill((255, 255, 255))
    grey = 225
    black = 100
    grey_tuple = (grey, grey, grey)
    black_tuple = (black, black, black)
    for y in range(0, height + 1, scale):
        pygame.draw.line(surface, grey_tuple, (0, y), (width, y))
    for x in range(0, width + 1, scale):
        pygame.draw.line(surface, grey_tuple, (x, 0), (x, height))
    pygame.draw.line(surface, black_tuple, (width // 2, 0), (width // 2, height))
    pygame.draw.line(surface, black_tuple, (0, height // 2), (width, height // 2))


def main():
    scale = 10
    min_max_x = 20
    min_max_y = 20
    width = min_max_x * 2 * scale
    height = min_max_y * 2 * scale

    pygame.init()

    while True:
        points = []
        expression = get_user_expression()
        print('USER expression:', expression)
        postfix = infix_to_postfix(expression)
        print('POSTFIX expression:', postfix)

        surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Graphing Calculator')
        draw_graph(surface, width, height, scale)

        x = -min_max_x
        while x < min_max_x:
            y = evaluate_postfix(postfix, x=x)
            draw_x = round(x * scale + width // 2)
            draw_y = round(-y * scale + height // 2)
            points.append((draw_x, draw_y))
            x += scale / 100
        pygame.draw.aalines(surface, (255, 0, 0), False, points)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if not done:
                pygame.display.flip()

        x = input('Would like to graph another? [y/n]: ')
        if x.lower() == 'n':
            pygame.quit()
            break


if __name__ == '__main__':
    main()
