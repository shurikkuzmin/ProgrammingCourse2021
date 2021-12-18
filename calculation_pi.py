#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:02:49 2021

@author: shurik
"""

import pygame
import random

pygame.init()

WINDOW = pygame.display.set_mode((500,500))
WINDOW.fill((0,0,0))


isActive = True

numPointsInCircle = 0
numPoints = 0
while isActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
    pygame.draw.circle(WINDOW, (255,140,0), (250,250), 250, 2)
    x = random.randint(0, 499)
    y = random.randint(0, 499)
    
    if (x - 250)**2 + (y - 250)**2 <= 250**2:
        numPointsInCircle = numPointsInCircle + 1
        pygame.draw.rect(WINDOW, (255,0,0), (x,y,1,1))
    else:
        pygame.draw.rect(WINDOW, (255,255,255), (x,y,1,1))
    
    numPoints = numPoints + 1
    
    pygame.display.update()
    print(4*numPointsInCircle/numPoints)
pygame.quit()
