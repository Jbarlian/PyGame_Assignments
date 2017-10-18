import sys
import pygame
from Shooter_Settings import Settings
from Shooter_Ship import Ship
import Game_Functions as gf
from pygame.sprite import Group
from Alien import Alien
from pygame.mixer import *
from GameStats import GameStats
from Button import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of aliens.
    # alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    music.load('Magic.mp3')
    music.play(loops=-1)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
        bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)


run_game()