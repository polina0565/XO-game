import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for ROW in range(6):
        for COL in range(1,5):
            print (COL, ROW)
            if mas[ROW][COL-1] == sign and mas[ROW][COL] == sign and mas[ROW][COL+1] == sign:
                return sign
    for COL in range(6):
        for ROW in range(1,5):
            if mas[COL-1][ROW] == sign and mas[COL][ROW] == sign and mas[COL+1][ROW] == sign:
                return sign
    if zeroes == 0:
        return 'Ничья'
    return False


pygame.init()

k = 0
l = 0
size_block = 100
margin = 10
width = height = size_block * 6 + margin * 7

win_size = (width, height)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Крестики-нолики")

black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
mas = [[0] * 6 for i in range(6)]
query = 0  # 1 2 3 4 5 6 7
game_over = False
TEXT = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if 0 == mas[row][col]:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
            if (query - 1) % 2 == 0:  # x
                game_over = check_win(mas, 'x')
            else:
                game_over = check_win(mas, 'o')
            if game_over == 'x':
                k += 1
                TEXT = "Победа крестиков " + str(k)
            elif game_over == 'o':
                l += 1
                TEXT = "Победа ноликов " + str(l)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 6 for i in range(6)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(6):
            for col in range(6):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('times new roman', 30)
        text1 = font.render(TEXT, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()
