import pygame
import sys

def check_win(mas,sign):
zeroes = 0
for row in mas:
zeroes+= row.count(0)
if row.count(sign)==3:
return sign
for col in range(3):
if mas [0] [col]==sign and mas[1][col]==sign and mas[2][col]==sign:
return sign
if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
return sign
if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
return sign
if zeroes==0:
return 'Piece'
return False



pygame.init()
block_size = 150
margin = 10
wigth = height = block_size*3 + margin*4

win_size = (wigth, height)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Крестики нолики")

pink = (250, 5, 34)
green = (0, 255, 0)
white = (255, 255, 255)
red = (130, 9, 21)
mas = [[0]*3 for i in range(3)]
query = 0 # 1 2 3 4 5 6 7


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit((0))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (block_size+margin)
            row = y_mouse // (block_size + margin)

            if query%2==(0):
               mas[row][col] = 'x'
else:
mas[row][col] = 'o'
query +=1

for row in range(3):
for col in range(3):
if mas[row][col]=='x':
color = red
elif mas[row][col]=='o':
color = green
else:
color = white
x = col*block_size + (col+1) * margin
y = row * block_size + (row + 1) * margin
pygame.draw.rect(screen, color, (x,y,block_size,block_size))
if color==red:
pygame.draw.line(screen,white, (x+5,y+5), (x+block_size-5,y+block_size-5),3)
pygame.draw.line(screen, white, (x + block_size - 5, y + 5), (x+5, y + block_size - 5), 3)
elif color == green:
pygame.draw.circle(screen,white, (x+block_size//2,y+block_size//2),block_size//2-3,3)
if (query-1)%2==0:#x
game_over = check_win(mas, 'x')
else:
game_over = check_win(mas, 'o')
    if game_over:






pygame.display.update()

