import numpy as np
import pygame

from pygame.locals import *

width = 640
height = 640

class sumo_robot:
    def __init__(self, enemy):
        self.speed = (0,0)
        self.mass = 5
        self.size = 80
        self.rad = self.size * np.sqrt(2)
        self.motor_speed = 0.1
        if enemy:
            self.angle = np.pi*1.5
            self.color = (255,0,0)
            self.x3 = (width/2)-40
            self.y3 = 100
            self.x4 = self.x3 + self.size
            self.y4 = self.y3
            self.x1 = self.x4
            self.y1 = self.y4+self.size
            self.x2 = self.x3
            self.y2 = self.y1
        else:
            self.angle = np.pi /2
            self.color = (0,0,255)
            self.x1 = (width/2)-40
            self.y1 = height - 180
            self.x2 = self.x1 + self.size
            self.y2 = self.y1
            self.x3 = self.x2
            self.y3 = self.y2+self.size
            self.x4 = self.x1
            self.y4 = self.y3

    def display(self):
        pygame.draw.polygon(screen, self.color, [
        [int(self.x1), int(self.y1)],
        [int(self.x2), int(self.y2)],
        [int(self.x3), int(self.y3)],
        [int(self.x4), int(self.y4)]], 5)

    def rotate_left(self):
        self.rotation_angle = 2*self.motor_speed/self.size
        self.ang01 = np.arctan2(self.y3 - self.y1, self.x1 - self.x3)
        self.ang02 = np.arctan2(self.y4 - self.y2, self.x2 - self.x4)

        self.ang1 = self.ang01 + self.rotation_angle
        if self.ang1 >= np.pi*2: self.ang1 -= (np.pi*2)
        elif self.ang1<0: self.ang1 += (np.pi*2)

        self.ang2 = self.ang02 + self.rotation_angle
        if self.ang2 >= np.pi*2: self.ang2 -= (np.pi*2)
        elif self.ang2<0: self.ang2 += (np.pi*2)

        self.x1 += self.rad * (np.cos(self.ang1)-np.cos(self.ang01))
        self.y1 -= self.rad * (np.sin(self.ang1)-np.sin(self.ang01))

        self.x2 += self.rad * (np.cos(self.ang2)-np.cos(self.ang02))
        self.y2 -= self.rad * (np.sin(self.ang2)-np.sin(self.ang02))

        self.x3 += self.rad * (np.cos(np.pi+self.ang1)-np.cos(np.pi+self.ang01))
        self.y3 -= self.rad * (np.sin(np.pi+self.ang1)-np.sin(np.pi+self.ang01))

        self.x4 += self.rad * (np.cos(np.pi+self.ang2)-np.cos(np.pi+self.ang02))
        self.y4 -= self.rad * (np.sin(np.pi+self.ang2)-np.sin(np.pi+self.ang02))

    def rotate_right(self):
        self.rotation_angle = -2*self.motor_speed/self.size
        self.ang01 = np.arctan2(self.y3 - self.y1, self.x1 - self.x3)
        self.ang02 = np.arctan2(self.y4 - self.y2, self.x2 - self.x4)

        self.ang1 = self.ang01 + self.rotation_angle
        if self.ang1 >= np.pi*2: self.ang1 -= (np.pi*2)
        elif self.ang1<0: self.ang1 += (np.pi*2)

        self.ang2 = self.ang02 + self.rotation_angle
        if self.ang2 >= np.pi*2: self.ang2 -= (np.pi*2)
        elif self.ang2<0: self.ang2 += (np.pi*2)

        self.x1 += self.rad * (np.cos(self.ang1)-np.cos(self.ang01))
        self.y1 -= self.rad * (np.sin(self.ang1)-np.sin(self.ang01))

        self.x2 += self.rad * (np.cos(self.ang2)-np.cos(self.ang02))
        self.y2 -= self.rad * (np.sin(self.ang2)-np.sin(self.ang02))

        self.x3 += self.rad * (np.cos(np.pi+self.ang1)-np.cos(np.pi+self.ang01))
        self.y3 -= self.rad * (np.sin(np.pi+self.ang1)-np.sin(np.pi+self.ang01))

        self.x4 += self.rad * (np.cos(np.pi+self.ang2)-np.cos(np.pi+self.ang02))
        self.y4 -= self.rad * (np.sin(np.pi+self.ang2)-np.sin(np.pi+self.ang02))

    def move_forward(self):
        self.direction = np.arctan2(self.y1-self.y4, self.x1-self.x4)
        self.x1 += np.cos(self.direction) * self.motor_speed
        self.y1 += np.sin(self.direction) * self.motor_speed
        self.x2 += np.cos(self.direction) * self.motor_speed
        self.y2 += np.sin(self.direction) * self.motor_speed
        self.x3 += np.cos(self.direction) * self.motor_speed
        self.y3 += np.sin(self.direction) * self.motor_speed
        self.x4 += np.cos(self.direction) * self.motor_speed
        self.y4 += np.sin(self.direction) * self.motor_speed

    def move_backward(self):
        self.direction = np.pi+np.arctan2(self.y1-self.y4, self.x1-self.x4)
        self.x1 += np.cos(self.direction) * self.motor_speed
        self.y1 += np.sin(self.direction) * self.motor_speed
        self.x2 += np.cos(self.direction) * self.motor_speed
        self.y2 += np.sin(self.direction) * self.motor_speed
        self.x3 += np.cos(self.direction) * self.motor_speed
        self.y3 += np.sin(self.direction) * self.motor_speed
        self.x4 += np.cos(self.direction) * self.motor_speed
        self.y4 += np.sin(self.direction) * self.motor_speed

pygame.init()
pygame.display.set_caption('Sumo robots')
screen = pygame.display.set_mode((width, height))
screen.fill(Color(0,0,0))

pygame.draw.circle(screen, (255,255,255), (320,320), 300, 30)

my_robot = sumo_robot(False)
en_robot = sumo_robot(True)

my_robot.display()
en_robot.display()

efw = False
ebw = False
ert = False
elt = False

mfw = False
mbw = False
mrt = False
mlt = False

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                elt = True
            if event.key == pygame.K_RIGHT:
                ert = True
            if event.key == pygame.K_UP:
                efw = True
            if event.key == pygame.K_DOWN:
                ebw = True
            if event.key == pygame.K_a:
                mlt = True
            if event.key == pygame.K_d:
                mrt = True
            if event.key == pygame.K_w:
                mfw = True
            if event.key == pygame.K_s:
                mbw = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                elt = False
            if event.key == pygame.K_RIGHT:
                ert = False
            if event.key == pygame.K_UP:
                efw = False
            if event.key == pygame.K_DOWN:
                ebw = False
            if event.key == pygame.K_a:
                mlt = False
            if event.key == pygame.K_d:
                mrt = False
            if event.key == pygame.K_w:
                mfw = False
            if event.key == pygame.K_s:
                mbw = False

    if efw: en_robot.move_forward()
    if ebw: en_robot.move_backward()
    if ert: en_robot.rotate_right()
    if elt: en_robot.rotate_left()
    if mfw: my_robot.move_forward()
    if mbw: my_robot.move_backward()
    if mrt: my_robot.rotate_right()
    if mlt: my_robot.rotate_left()
    screen.fill(Color(0,0,0))
    pygame.draw.circle(screen, (255,255,255), (320,320), 300, 30)
    my_robot.display()
    en_robot.display()
    pygame.display.update()
