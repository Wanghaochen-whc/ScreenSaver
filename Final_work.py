import pygame
import random


# Set the screen width and height
screen_width = 800
screen_height = 600

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

# Set the number of stars, their movement speed, and initialize the star column
number_of_stars = 100
speed = 0.5
stars = []


def new_star(screen_width, screen_height) -> list:
    """
    This function creates a new star with random X and Y coordinates within a specified range,
    a fixed Z - distance of 256, and an initial color value of 0.
    """
    # Generate random X and Y coordinates within the specified intervals
    x = random.randint(-screen_width // 2, screen_width // 2)
    y = random.randint(-screen_height // 2, screen_height // 2)

    # The Z - distance is always 256
    z = 256

    # The initial color is 0
    color = 0

    # Create a list to represent the star
    star = [x, y, z, color]

    return star


def move_and_check(star: list, screen_width, screen_height, speed) -> list:
    x = star[0]
    y = star[1]

    star[2] -= speed  # Change Z coordinate

    # Convert to coordinates in the screen coordinate system
    screen_x = int((x / star[2]) * screen_width + screen_width / 2)
    screen_y = int((y / star[2]) * screen_height + screen_height / 2)

    # If the coordinates go beyond the screen, we generate a new star.
    if screen_x < 0 or screen_x > screen_width or screen_y < 0 or screen_y > screen_height or star[2] <= 0:
        star = new_star(screen_width, screen_height)

    # If the color has not reached maximum brightness, increase the color.
    if star[3] < 255:
        star[3] += 0.15

    #  If suddenly the color becomes more than acceptable, then set it to 255
    if star[3] > 255:
        star[3] = 255

    return star


def draw_star(star: list, screen) -> None:
    x = int((star[0] / star[2]) * screen.get_width() + screen.get_width() / 2)
    y = int((star[1] / star[2]) * screen.get_height() + screen.get_height() / 2)
    pygame.draw.circle(screen, (int(star[3]), int(star[3]), int(star[3])), (x, y), 3)


# Generate initial stars
for i in range(0, number_of_stars):
    stars.append(new_star(screen_width, screen_height))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(0, number_of_stars):
        s = stars[i]
        # Move the star and check if it still appear
        s = move_and_check(s, screen_width, screen_height, speed)
        stars[i] = s
        # draw the star on the screen
        draw_star(s, screen)

    pygame.display.flip()

pygame.quit()