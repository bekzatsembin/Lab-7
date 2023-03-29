import pygame

pygame.init()

# Set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Set up the ball
ball_radius = 25
ball_pos = [screen_width//2, screen_height//2]

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the clock for the game loop
clock = pygame.time.Clock()

# The game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_pos[1] - 20 >= ball_radius:
                    ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                if ball_pos[1] + 20 <= screen_height - ball_radius:
                    ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                if ball_pos[0] - 20 >= ball_radius:
                    ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_pos[0] + 20 <= screen_width - ball_radius:
                    ball_pos[0] += 20

    # Draw the ball and update the display
    screen.fill(white)
    pygame.draw.circle(screen, red, ball_pos, ball_radius)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
