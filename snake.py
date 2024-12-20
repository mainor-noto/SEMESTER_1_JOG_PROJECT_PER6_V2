import pygame, random


pygame.init()
# Set display window
# TODO: create a WINDOW_WIDTH variable and assign it a value of 600
WINDOW_WIDTH = 600
# TODO: create a WINDOW_HEIGHT variable and assign it a value of 600
WINDOW_HEIGHT = 600
# TODO: create a display_surface variable and assign it from pygame.display.set_mode passing
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# in a tuple of WINDOW_WIDTH and WINDOW_HEIGHT
# TODO: call pygame.display.set_caption() passing in "~~Snake~~"
pygame.display.set_caption("Snake")

# Set FSP and clock
# TODO: create a FPS variable and assign it a value of 20
FPS = 20
# TODO: create a clock variable and assign it a value of pygame.time.Clock()
pygame.time.Clock()

# Set game values
# TODO: create a SNAKE_SIZE variable and assign it a value of 20
SNAKE_SIZE = 20
# TODO: create a head_x variable and assign it a value of WINDOW_WIDTH // 2
head_x = WINDOW_WIDTH//2
# TODO: repeat for head_y and assign it a value of WINDOW_HEIGHT // 2 + 100
head_y = WINDOW_HEIGHT // 2+100
# TODO: create a snake_dx variable and assign it a value of 0
snake_dx = 0
# TODO: repeat for snake_dy
snake_dy = 0
# TODO: create a score variable and assign it a value of 0
score = 0

# Set colors
# TODO: create GREEN, RED and WHITE tuples for the colors.  Use Standard RGB settings for those
# TODO: create a DARKGREEN tuple and set to (10, 50, 10)
DARKGREEN = (10,50,10)
# TODO: create a DARKRED tuple and set to (150, 0, 0)
DARKRED = (150,0,0)
GREEN = (0, 255, 0)
RED = (255,0,0)
WHITE = (255,255,255)
# Set fonts
font = pygame.font.SysFont('gabriola', 48)


# Set text

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        # TODO: add an if condition for "topleft" similar to the if condition for "center"
    return text, rect


# TODO: Here is a usage example for the rest of the text and rectangles that you'll create.
title_text, title_rect = create_text_and_rect("~~Snake~~",DARKGREEN, DARKRED,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# TODO: unpack the tuple from create_text_and_rect into a score_text and score_rect variable
score_text, score_rect = create_text_and_rect("Score:"+ str(score),GREEN, DARKRED,topleft= (10,10))
# TODO: text is "Score: " + str(score)
# TODO: color is GREEN
# TODO: background_color is DARKRED
# TODO: locations are topleft=(10, 10)

# TODO: unpack the tuple from create_text_and_rect into a game_over_text and game_over_rect variable
# TODO: text is "GAMEOVER"
game_over_text, game_over_rect = create_text_and_rect("GAMEOVER" ,RED, DARKGREEN,center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
# TODO: color is RED
# TODO: background_color is DARKGREEN
# TODO: locations are center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# TODO: unpack the tuple from create_text_and_rect into a continue_text and continue_rect variable
continue_text, continue_rect = create_text_and_rect("press any key to play again", RED,DARKGREEN, center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT //2 + 64))
# TODO: text is "Press any key to play again"
# TODO: color is RED
# TODO: background_color is DARKGREEN
# TODO: locations are center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)


# Set sounds and music
# TODO: create a variable called pick_up_sound and set to pygame.mixer.Sound("pick_up_sound.wav")
# TODO: make sure you have pick_up_sound.wav in the same folder as snake.py.
# TODO: make sure both of your files are not in the .venv folder.  Otherwise I won't see what you've done.
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
# TODO: create a variable called apple_coord and set to (500, 500, SNAKE_SIZE, SNAKE_SIZE)
# TODO: create a variable called apple_rect and set to pygame.draw.rect(display_surface, RED, apple_coord)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface,DARKRED, apple_coord )
# TODO: create a variable called head_coord and set to (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
# TODO: create a variable called head_rect and set to pygame.draw.rect(display_surface, GREEN, head_coord)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
# TODO: create a variable called body_coords and set to an empty list
body_coords = []

# The main game loop
running = True,
is_paused = False,


def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        # TODO: check if key is equal to pygame.K_LEFT
            # TODO: if so set snake_dx to -1 * SNAKE_SIZE and snake_dy = 0
        if key == pygame.K_LEFT:
            snake_dx = -1 * SNAKE_SIZE
            snake_dy = 0
        # TODO: check if key is equal to pygame.K_RIGHT
            # TODO: if so set snake_dx to SNAKE_SIZE and snake_dy to 0
        if key == pygame.K_RIGHT:
            snake_dx = SNAKE_SIZE
            snake_dy = 0
        # TODO: check if key is equal to pygame.K_UP
            # TODO: if so set snake_dx to 0 and snake_dy to -1 * SNAKE_SIZE
        if key == pygame.K_UP:
            snake_dx = 0
            snake_dy = -1 * SNAKE_SIZE
        # TODO: check if key is equal to pygame.K_DOWN
            # TODO: if so set snake_dx to 0 and snake_dy to SNAKE_SIZE
        if key == pygame.K_DOWN:
            snake_dx = 0
            snake_dy = SNAKE_SIZE



def check_quit(event):
    global running
    if event.type == pygame.quit:
        running = False
    # TODO: if event is equal to pygame.QUIT  set running to false


def check_events():
    global running
    # TODO: create a for loop events is the variable pygame.event.get() is the list
    for event in pygame.event.get():
        check_quit(event)
        move_snake(event)
        # TODO: call check_quit(event)
        # TODO: call move_snake(event)
 # TODO: remove this pass when done.

def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    # TODO: call body_coords.insert() method and pass in 0, head_coord
    body_coords.insert(0, head_coord)
    # TODO: call body_coords.pop()
    body_coords.pop()
    # TODO: add snake_dx to head_x
    head_x += snake_dx
    # TODO: add snake_dy to head_y
    head_y += snake_dy
    # TODO: set head_coord to (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
    # TODO: if event.type is equal to pygame.KEYDOWN
    if event.type == pygame.KEYDOWN:
        score = 0
        head_x = WINDOW_WIDTH //2
        head_y = WINDOW_HEIGHT // 2 + 100
        head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        snake_dy = 0
        snake_dx = 0
        is_paused = False
        # TODO: set head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: set body_coords to an empty list
        # TODO: set snake_dx to 0
        # TODO: set snake_dy to 0
        # TODO: set is_paused to False

def check_end_game_after_game_over(event):
    global is_paused
    global running
    # TODO: if event.type is equal to pygame.QUIT
    if event.type == pygame.QUIT:
        is_paused = False
        running = False
        # TODO: set is_paused to False
        # TODO: set running to False



def check_game_over():
    global head_rect
    global head_coord
    global body_coords
    global running
    global is_paused
    # TODO: if head_rect.left is negative or head_rect.right is greater than WINDOW_WIDTH or head_rect.top is negative or head_rect.bottom is greater than WINDOW_HEIGHT
    # or head_coord in body_coords
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                reset_game_after_game_over(event)
                check_end_game_after_game_over(event)

def check_collisions():
    global score, apple_x, apple_y, apple_coord, body_coords
    # TODO: if head_rect.colliderect(apple_rect)
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        # TODO: add 1 to the score
        # TODO: call pick_up_sound.play()
        # TODO: set apple_x to random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        # TODO: set apple_y to random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        # TODO: set apple_coord to (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: call body_coords.append(head_coord)
        pass # TODO: remove this pass when done.

def blit_hud():
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.

def blit_assets():
    # TODO: for body in body_coords:
        # TODO: call pygame.draw.rect(display_surface, DARKGREEN, body)
    # TODO: set head_rect to pygame.draw.rect(display_surface, GREEN, head_coord)
    # TODO: set apple_rect to pygame.draw.rect(display_surface, RED, apple_coord)
    pass  # TODO: remove this pass when done.

def update_display_and_tick_clock():
    # TODO: call pygame.display.update()
    # TODO: call clock.tick(FPS)
    pass  # TODO: remove this pass when done.

while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    # TODO: set score_text to font.render("Score: " + str(score), True, GREEN, DARKRED)

    # Fill the surface
    # TODO: call display_surface.fill(WHITE)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()