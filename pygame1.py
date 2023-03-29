# Imports the Pygame and time libraries.
import pygame
import time

# Initializes Pygame.
pygame.init()

window_size = (836,836)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey Mouse Clock")

# Initializes the clock object for Pygame.
clock = pygame.time.Clock()
mickey = pygame.image.load("main-clock.png")



minute_hand = pygame.image.load("righthand.png")
second_hand = pygame.image.load("lefthand.png")

# Sets the initial positions of the minute and second hands at the center of the window.
minute_hand_pos = (window_size[0] // 2, window_size[1] // 2)
second_hand_pos = (window_size[0] // 2, window_size[1] // 2)

# Creates an infinite loop until the user exits the program.
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

# Gets the current time in minutes and seconds using the time.localtime() function.
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

# Calculates the angles of the minute and second hands using the current time.
    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

# Rotates the images of the minute and second hands according to their respective angles.
    minute_hand_rotated = pygame.transform.rotate(minute_hand, 90-minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand, 90-second_angle)

# Calculates the new positions of the minute and second hands after they have been rotated.
    minute_hand_pos = (window_size[0] // 2 - minute_hand_rotated.get_width() // 2,
                       window_size[1] // 2 - minute_hand_rotated.get_height() // 2)
    second_hand_pos = (window_size[0] // 2 - second_hand_rotated.get_width() // 2,
                       window_size[1] // 2 - second_hand_rotated.get_height() // 2)

# Fills the window with a white color.
    window.fill((255, 255, 255))

# Blits the images of Mickey Mouse, minute hand, and second hand onto the window.
    window.blit(mickey, (0,0))
    window.blit(minute_hand_rotated, minute_hand_pos)
    window.blit(second_hand_rotated, second_hand_pos)

# Flips the display to show the updated window.
    pygame.display.flip()

# Pauses for 1000 milliseconds (1 second) using the pygame.time.delay() function.    
    pygame.time.delay(1000)
    
