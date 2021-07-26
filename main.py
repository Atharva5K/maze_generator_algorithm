import pygame
from numpy import random

pygame.init()

scree_dim = 800
x=110
y=100
screen = pygame.display.set_mode((scree_dim,scree_dim))
pygame.display.set_caption("MAZE")
done = True
stack_ = []
visited = []
temp = []
init = False
start = True
for i in range (100,710,10) :
    temp.append(i)
'''
for i in temp:
    visited.append((i,100))
    visited.append((i,700))
    visited.append((100,i))
    visited.append((700,i))
'''
def random_lines():
    global x,y,stack_,visited,init,start
    while start :
        if init:
            no = random.randint(1,5)
        else:
            no=2
            init = True

        if no == 1 and x+10<=700 and visited.count((x+10,y))==0:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x+10, y), 1)
            x+=10
            visited.append((x,y))

            if visited.count((x+10,y))==0 and x+10<=700:
                stack_.append((x+10, y))
            if visited.count((x,y+10))==0 and y+10<=700:
                stack_.append((x, y+10))
            if visited.count((x,y-10))==0 and y-10>=100:
                stack_.append((x, y-10))

            pygame.display.update()
            break
        elif no == 2 and y+10<=700 and visited.count((x,y+10))==0:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y+10), 1)
            y+=10
            visited.append((x, y))

            if visited.count((x+10,y))==0 and x+10<=700:
                stack_.append((x+10, y))
            if visited.count((x,y+10))==0 and y+10<=700:
                stack_.append((x, y+10))
            if visited.count((x-10,y))==0 and x-10>=100:
                stack_.append((x-10, y))

            pygame.display.update()
            break
        elif no == 3 and x-10>=100 and visited.count((x-10,y))==0:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x-10, y), 1)
            x-=10
            visited.append((x, y))

            if visited.count((x-10,y))==0 and x-10>=100:
                stack_.append((x-10, y))
            if visited.count((x,y+10))==0 and y+10<=700:
                stack_.append((x, y+10))
            if visited.count((x,y-10))==0 and y-10>=100:
                stack_.append((x, y-10))

            pygame.display.update()
            break
        elif no == 4 and y-10>=100 and visited.count((x,y-10))==0:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y - 10), 1)
            y-=10
            visited.append((x, y))

            if visited.count((x+10,y))==0 and x+10<=700:
                stack_.append((x+10, y))
            if visited.count((x,y-10))==0 and y-10>=100:
                stack_.append((x, y-10))
            if visited.count((x-10,y))==0 and x-10>=100:
                stack_.append((x-10, y))

            pygame.display.update()
            break
        else:
            if len(stack_) == 0 :
                start = False
            else :
                (x,y) = stack_.pop()
        #print(stack_)
        #break

pygame.draw.rect(screen,(255,255,255),(100,100,600,600),1)
pygame.display.update()
clock = pygame.time.Clock()

while done :
    clock.tick(30)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = False
    random_lines()
pygame.quit()