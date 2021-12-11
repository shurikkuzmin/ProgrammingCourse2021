#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:02:49 2021

@author: shurik
"""

import pygame

pygame.init()

WINDOW = pygame.display.set_mode((500,500))

pygame.display.update()


isActive = True
while isActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
pygame.quit()
