#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import (
        K_ESCAPE,
        QUIT,
        KEYDOWN,
        KMOD_NONE,
        KMOD_SHIFT,
)
from player import *
from enemii import *
import random
from projectill import *
import sys
#import thorpy
from ui import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,1024), pygame.FULLSCREEN)
    back = pygame.Surface(screen.get_size())
    area = pygame.Rect((0,0),(1000,1024))
    back.fill((0,0,90))
    back = back.convert()
    screen.blit(back,(0,0))

    clock = pygame.time.Clock()

    score = 0
    game_loop = True
    player_alive = True
    player_lives = 3
    if len(sys.argv) == 2:
        player_lives = int(sys.argv[1])
    player = Player(area)
    ui_here = Ui(screen)
    playt = 1
    enemy_list = pygame.sprite.Group()
    ebullets = pygame.sprite.Group()
    count = 0
    kt = 0
    kills = 0
    i = 0
    j = 0
    locker = 0
    while game_loop:
        if player_alive is False:
            if kt == 0:
                score -= 100
                if score < 0:
                    score = 0
                player.face.fill((100,100,100))
                kt = int(playt)
            if int(playt) >= kt + 5:
                player_alive = True
                kt = 0
                player.face.fill((255,210,255))

        if not enemy_list:
            if i == 0:
                enemy_list.add(Enemy(place = 250, side = "l", xspeed = 1, hpboost = 20))
                enemy_list.add(Enemy(place = 750, ft = "cw", xspeed = 1, hpboost = 20))
                enemy_list.add(Enemy(place = 250, side = "l", xspeed = 1, hpboost = 20, wait = 401, stop = 376))
                enemy_list.add(Enemy(place = 750, ft = "cw", xspeed = 1, hpboost = 20, wait = 502, stop = 472))
                enemy_list.add(Enemy(place = 250, side = "l", xspeed = 1, hpboost = 20, wait = 803, stop = 512))
                enemy_list.add(Enemy(place = 750, ft = "cw", xspeed = 1, hpboost = 20, wait = 1104, stop = 126))
                enemy_list.add(Enemy(place = 250, side = "l", xspeed = 1, hpboost = 20, wait = 1805, stop = 126))
                enemy_list.add(Enemy(place = 750, ft = "cw", xspeed = 1, hpboost = 20, wait = 1803, stop = 212))
                enemy_list.add(Enemy(place = 250, side = "l", xspeed = 1, hpboost = 20, wait = 2236, stop = 412))
                enemy_list.add(Enemy(place = 750, ft = "cw", xspeed = 1, hpboost = 20, wait = 2468, stop = 312))
                locker = int(playt)
                i = 0
            elif i == 1:
                count = 10
                i += 1
            elif i == 2:
                count = 15
                i += 1
            elif i == 3:
                count = 20
                i += 1
            elif i == 4:
                count = 25
                i += 1
                #TODO replace with something a tad bit special later ツ
            elif i >= 5:
                i = 0

        #count = 1

        milsec = clock.tick(200)
        playt += milsec/1000.0
        if int(playt)/int(playt) == 1:
            score += 1

        if int(playt) == (locker - 60):
            for enemy in enemy_list:
                enemy.kill()

        #usr_in = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                game_loop = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_loop = False

        if player_lives <= 0:
            game_loop = False


        usr_in = pygame.key.get_pressed()
        #mods = pygame.key.get_mods()
        player.normal_movement(usr_in)

        for i in enemy_list:
            for pull in player.pullets:
                if i.collision(pull,3):
                    kills += 1
                    score += 20
            for pr in player.pread:
                if i.collision(pr,1):
                    kills += 1
                    score += 20

            i.move()
            i.roshoot(ebullets)
            if player_alive is True:
                #for j in i.bullets:
                if player.collision(i,None):
                    player_alive = False
                    player_lives -= 1

            if i.rect.centerx <= 1000:
                screen.blit(i.face,i.rect)
        i = 0
        for bull in ebullets:
            bull.erestrifire()
            #bull.efire()
            #screen.blit(bull.face, bull.rect)
            if bull.px <= 1000:
                pygame.draw.circle(screen,(255,50,50,1),(bull.rect.x,bull.rect.y),8,0)
            if player_alive is True:
                if player.collision(None,bull):
                    player_alive = False
                    player_lives -= 1

            '''
            for pull in player.pullets:
                bull.collision(pull)
            for pr in player.pread:
                bull.collision(pr)
            '''


        for pull in player.pullets:
            pull.pfire()
            #screen.blit(bull.face, bull.rect)
            if pull.px <= 1000:
                pygame.draw.circle(screen,(255,50,255,200),(pull.rect.x,pull.rect.y),9,0)
            #if bull.rect.y > 1048:
                #bull.kill()
        for pr in player.pread:
            pr.plrbeam()
            #screen.blit(bull.face, bull.rect)
            if pr.px <= 1000:
                pygame.draw.circle(screen,(20,50,255,200),(pr.rect.x,pr.rect.y),7,0)
            #if bull.rect.y > 1048:
                #bull.kill()

        '''
        if(kills>10 and int(kills/3)%3 == 0):
            player.upgrades += 1
            if player.upgrades < 1024:
                if player.upgrades%5 == 0:
                    player.spreads += 1
                elif player.upgrades%7 == 0:
                    if player.defhold > 2:
                        player.defhold -= 1
                else:
                    if player.shots < 10:
                        player.shots+=1
        '''
        screen.blit(player.face,player.rec)
        pygame.display.update()
        screen.fill((0,0,0))
        screen.blit(back,(0,0))
        screen.blit(ui_here.ui,ui_here.rect)
        ui_here.texty_text(score,player_lives)

    pygame.quit()



main()
