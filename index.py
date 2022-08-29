import pygame, sys
from pygame import mixer #mixer es para los sonidos
from pynput import keyboard as kb
from button import Button
from tkinter import font
from battle import battle
from snake import snake

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("./assets/img/backgroundIndex.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/font/8bit_wonder/8-BIT WONDER.TTF", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(645, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("GameBoy CESDE", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(405, 63))

        BATTLE_BUTTON = Button(image=pygame.image.load("assets/img/Play Rect.png"), pos=(400, 156), 
                            text_input="BATTLE", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        SNAKE_BUTTON = Button(image=pygame.image.load("assets/img/Play Rect.png"), pos=(400, 250), 
                            text_input="SNAKE", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        EXIT_BUTTON = Button(image=pygame.image.load("assets/img/Play Rect.png"), pos=(400, 344), 
                            text_input="EXIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BATTLE_BUTTON, SNAKE_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BATTLE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    battle()
                if SNAKE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    snake()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()