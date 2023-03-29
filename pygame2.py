import pygame

pygame.init()

# Set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

# Load some music tracks
track_list = ["track1.mp3", "track2.mp3", "track3.mp3"]
current_track = 0

# Load some images for the buttons
play_img = pygame.image.load("play.png")
stop_img = pygame.image.load("stop.png")
next_img = pygame.image.load("next.png")
prev_img = pygame.image.load("prev.png")

# Resize all images to the same size
button_size = (100, 50)
play_img = pygame.transform.scale(play_img, button_size)
stop_img = pygame.transform.scale(stop_img, button_size)
next_img = pygame.transform.scale(next_img, button_size)
prev_img = pygame.transform.scale(prev_img, button_size)

# Define the positions of the buttons
button_margin = 10
play_pos = (button_margin, screen_height - button_size[1] - button_margin)
stop_pos = (play_pos[0] + button_size[0] + button_margin, screen_height - button_size[1] - button_margin)
next_pos = (screen_width - button_size[0] - button_margin, screen_height - button_size[1] - button_margin)
prev_pos = (next_pos[0] - button_size[0] - button_margin, screen_height - button_size[1] - button_margin)

# Load the current track and create a pygame.mixer.Sound object
current_sound = pygame.mixer.Sound(track_list[current_track])

# Set up the clock for the game loop
clock = pygame.time.Clock()

# Set up some variables for tracking the player state
playing = False
stopped = True

# The game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if stopped:
                    playing = True
                    stopped = False
                    current_sound.play()
                elif playing:
                    playing = False
                    stopped = True
                    current_sound.stop()
            elif event.key == pygame.K_RIGHT:
                if current_track < len(track_list) - 1:
                    current_track += 1
                    current_sound.stop()
                    current_sound = pygame.mixer.Sound(track_list[current_track])
                    if not stopped:
                        current_sound.play()
                elif event.key == pygame.K_LEFT:
                    if current_track > 0:
                        current_track -= 1
                        current_sound.stop()
                        current_sound = pygame.mixer.Sound(track_list[current_track])
                        if not stopped:
                            current_sound.play()

    # Update the display
    screen.fill((255, 255, 255))
    screen.blit(play_img, play_pos)
    screen.blit(stop_img, stop_pos)
    screen.blit(next_img, next_pos)
    screen.blit(prev_img, prev_pos)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
