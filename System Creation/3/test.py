import pygame
import random 
pygame.init()
screen = pygame.display.set_mode((640, 480))


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def draw_tree(x, y):
    # tree trunk (50 wide and 100 tall)
    pygame.draw.rect(screen, (117, 90, 0), (x, y-100, 50, 100))
    # leaves are a circle
    pygame.draw.circle(screen, (27, 117, 0), (x+25, y-120), 50)


def draw_house(x, y):
    # pink house
    pygame.draw.rect(screen, (255, 171, 244), (x, y-180, 200, 180))
    # brown door
    pygame.draw.rect(screen, (89, 71, 0), (x+80, y-60, 40, 60))
    # yellow door knob
    pygame.draw.circle(screen, (255, 204, 0), (x+112, y-30), 4)
    # triangle roof
    pygame.draw.polygon(screen, (125, 125, 125), ((
        x, y-180), (x+100, y-250), (x+200, y-180)))
    draw_window(x+20, y-90)
    draw_window(x+130, y-90)
    draw_window(x+75, y-180)


def draw_window(x, y):
    # glass
    pygame.draw.rect(screen, random_color(), (x, y-50, 50, 50))
    # frame
    pygame.draw.rect(screen, (0, 0, 0), (x, y-50, 50, 50), 5)
    pygame.draw.rect(screen, (0, 0, 0), (x+23, y-50, 5, 50))
    pygame.draw.rect(screen, (0, 0, 0), (x, y-27, 50, 5))


# this function is able to draw clouds of different sizes
def draw_cloud(x, y, size):
    # put int() around any multiplications by decimals to get rid of this warning:
    # DeprecationWarning: integer argument expected, got float
    pygame.draw.circle(screen, (255, 255, 255), (x, y), int(size*.5))
    pygame.draw.circle(screen, (255, 255, 255),
                       (int(x+size*.5), y), int(size*.6))
    pygame.draw.circle(screen, (255, 255, 255),
                       (x+size, int(y-size*.1)), int(size*.4))

def draw_butterfly(x, y, size):
    pygame.draw.polygon(screen, random_color(), [(x + 10 * size, y), (x + 20 * size,  y - 10 * size), (x + 60 * size, y - 10 * size), (x + 20 * size, y + 30 * size)])
    pygame.draw.polygon(screen, random_color(), [(x + 20 * size, y+ 30 * size), (x + 40 * size, y + 40 * size), (x + 40 * size, y + 70 * size), (x + 10 * size, y + 50 * size)])
    pygame.draw.polygon(screen, random_color(), [(x + 10 * size, y), (x, y - 10 * size), (x - 40 * size, y - 10 * size), (x, y + 30 * size)])
    pygame.draw.polygon(screen, random_color(), [(x, y + 30 * size), (x - 20 * size, y + 40 * size), (x - 20 * size, y + 70 * size), (x + 10 * size, y + 50 * size)])
    pygame.draw.ellipse(screen, random_color(), (x, y, 20 * size, 50 * size))
    pygame.draw.arc(screen, (0,0,0), (x, y - 10 * size, 10 * size, 20 * size), 0, 1.5707, 1 * size)
    pygame.draw.arc(screen, (0,0,0), (x + 10 * size, y - 10 * size, 10 * size, 20 * size), 1.5707, 3.14159, 1 * size)


# green ground
pygame.draw.rect(screen, (0, 160, 3), (0, 400, 640, 80))
# light blue sky
pygame.draw.rect(screen, (100, 200, 255), (0, 0, 640, 400))

draw_tree(60, 400)  # x and y location are the bottom left of tree trunk
draw_tree(550, 400)
draw_tree(30, 450)
draw_tree(580, 450)
draw_tree(450, 400)

draw_house(225, 400)

draw_cloud(60, 120, 80)
draw_cloud(200, 50, 40)
draw_cloud(500, 100, 100)
draw_cloud(300, 80, 60)

draw_butterfly(570, 300, 1)
draw_butterfly(100, 200, 2)
draw_butterfly(200, 100, 1)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()