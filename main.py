import random
import pygame
import os

pygame.init()

width = 1200
height = 700

# bringing all the images of the animation in one obj

path = "explosions/PNG"
files = os.listdir(path)
explosions = {}
for i in range(len(files)+1):
    if i==0:
        pass
    else:
        explosions.__setitem__(f"explosion{i}",os.listdir(f"{path}/Explosion_{i}"))

# main display function from here
display = pygame.display.set_mode((width,height))

blastlist = []


# creating the gameloop
def gameloop(display):
    def fireevents(event,method,e):
        if e.type == event:
            method()
    exit_game = False
    while not exit_game:
        display.fill("white")
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                exit_game=True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    fireevents(pygame.K_1,blast(explosions,f"explosion1",display,1),e)
                if e.key == pygame.K_2:
                    fireevents(pygame.K_1,blast(explosions,f"explosion2",display,2),e)
                if e.key == pygame.K_3:
                    fireevents(pygame.K_1,blast(explosions,f"explosion3",display,3),e)
                if e.key == pygame.K_4:
                    fireevents(pygame.K_1,blast(explosions,f"explosion4",display,4),e)
                if e.key == pygame.K_5:
                    fireevents(pygame.K_1,blast(explosions,f"explosion5",display,5),e)
                if e.key == pygame.K_6:
                    fireevents(pygame.K_1,blast(explosions,f"explosion6",display,6),e)
                if e.key == pygame.K_7:
                    fireevents(pygame.K_1,blast(explosions,f"explosion7",display,7),e)
                if e.key == pygame.K_8:
                    fireevents(pygame.K_1,blast(explosions,f"explosion8",display,8),e)
                if e.key == pygame.K_9:
                    fireevents(pygame.K_1,blast(explosions,f"explosion9",display,9),e)
                if e.key == pygame.K_c:
                    display.fill("white")
        
        pygame.display.update()


def blast(explosions,name,display,num):
    clock = pygame.time.Clock()
    x = random.randint(10,width-100)
    y = random.randint(10,height-500)
    try:
        if num==4 or num==7:
            path = f"explosions/PNG/Explosion_{num}/1/"
            bombimages = os.listdir(f"explosions/PNG/Explosion_{num}/1")
        else:
            path = f"explosions/PNG/Explosion_{num}/"
            bombimages = explosions[name]
        print(bombimages)
        for i in range(len(bombimages)):
            image = pygame.image.load(path+bombimages[i])
            display.blit(image,(x,y))
            pygame.display.update()
            clock.tick(25)
        display.fill("white")
    except Exception as e:
        print(e)

gameloop(display)



