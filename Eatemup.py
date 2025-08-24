import pygame
import random
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Supermarket Hole.io")

# Initialize fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (220, 220, 220)
GOLD = (255, 215, 0)
DARK_GREY = (100, 100, 100)
DARK_BLUE = (0, 0, 139)
LIGHT_BLUE = (135, 206, 250)
DARK_GREEN = (0, 100, 0)
RED_ORANGE = (255, 69, 0)

# Game states
MENU = 0
CHARACTER_MENU = 1
PLAYING = 2
game_state = MENU
selected_character = None

# Menu button class
class MenuButton:
    def __init__(self, text, pos, size=(200, 50)):
        self.text = text
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.hover = False
       
    def draw(self, screen):
        color = LIGHT_BLUE if self.hover else DARK_BLUE
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)
       
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
   
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

# Character selection button class
class CharacterButton:
    def __init__(self, character, pos):
        self.character = character
        self.rect = pygame.Rect(pos[0], pos[1], 200, 250)
        self.hover = False
       
    def draw(self, screen):
        # Draw button background
        color = GOLD if self.hover else LIGHT_BLUE
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)
       
        # Draw character name
        name_text = font.render(self.character['name'], True, WHITE)
        name_rect = name_text.get_rect(center=(self.rect.centerx, self.rect.bottom - 60))
        screen.blit(name_text, name_rect)
       
        # Draw description
        desc_text = font.render(self.character['description'], True, WHITE)
        desc_rect = desc_text.get_rect(center=(self.rect.centerx, self.rect.bottom - 30))
        screen.blit(desc_text, desc_rect)
       
        # Draw stats
        stats_text = font.render(f"Speed: {self.character['speed']} | HP: {self.character['hp']}", True, WHITE)
        stats_rect = stats_text.get_rect(center=(self.rect.centerx, self.rect.bottom - 10))
        screen.blit(stats_text, stats_rect)
   
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

# Particle effects class
class Particle:
    def __init__(self, x, y, color, size, speed, angle):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.angle = angle
        self.lifetime = 50

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.size -= 0.1
        self.lifetime -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Define character attributes
characters = {
    'charles': {
        'name': 'Charles',
        'speed': 5,
        'hp': 100,
        'radius': 30,
        'description': 'A balanced character with good speed and health'
    },
    'robot': {
        'name': 'Robot',
        'speed': 7,
        'hp': 120,
        'radius': 32,
        'description': 'Fast and agile with moderate health'
    },
    'wizard': {
        'name': 'Wizard',
        'speed': 6,
        'hp': 110,
        'radius': 31,
        'description': 'Magical abilities with balanced stats'
    },
    'dragon': {
        'name': 'Dragon',
        'speed': 4,
        'hp': 150,
        'radius': 35,
        'description': 'Large and powerful with high health'
    }
}

# Initialize character buttons
character_buttons = []
for i, char in enumerate(characters.values()):
    x = (i % 2) * 300 + 150
    y = (i // 2) * 300 + 150
    button = CharacterButton(char, (x, y))
    character_buttons.append(button)

# Initialize menu buttons
start_button = MenuButton("Start Game", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2))
quit_button = MenuButton("Quit", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 100))

# Game variables
hole_pos = [0, 0]  # World coordinates
hole_radius = 30
hole_growth_rate = 0.2
food_list = []
particles = []
score = 0
max_hp = 100
hp = max_hp
food_cooldown = 0
obstacle_cooldown = 0
FOOD_COOLDOWN = 30
OBSTACLE_COOLDOWN = 60
camera_pos = [0, 0]
CAMERA_SPEED = 5
MAP_SIZE = 100
TILE_SIZE = 50
map_tiles = {}

# Food types and their properties
food_types = {
    'apple': {
        'radius': 15,
        'color': (255, 0, 0),
        'points': 10,
        'speed': 0,
        'effect': 'none',
        'effect_duration': 0,
        'glow_color': (255, 100, 100),
        'description': 'Basic food item'
    },
    'banana': {
        'radius': 20,
        'color': (255, 255, 0),
        'points': 15,
        'speed': 0,
        'effect': 'speed_boost',
        'effect_duration': 500,
        'glow_color': (255, 255, 100),
        'description': 'Increases your movement speed'
    },
    'pizza': {
        'radius': 30,
        'color': (255, 128, 0),
        'points': 25,
        'speed': 0,
        'effect': 'hp_restore',
        'effect_duration': 0,
        'glow_color': (255, 200, 150),
        'description': 'Restores health'
    },
    'strawberry': {
        'radius': 18,
        'color': (255, 0, 128),
        'points': 12,
        'speed': 0,
        'effect': 'hp_boost',
        'effect_duration': 0,
        'glow_color': (255, 100, 200),
        'description': 'Increases max health'
    },
    'sushi': {
        'radius': 25,
        'color': (255, 182, 193),
        'points': 22,
        'speed': 1,
        'effect': 'speed_boost',
        'effect_duration': 300,
        'glow_color': (255, 200, 200),
        'description': 'Temporary speed boost'
    },
    'taco': {
        'radius': 25,
        'color': (255, 128, 0),
        'points': 22,
        'speed': 1,
        'effect': 'speed_boost',
        'effect_duration': 400,
        'glow_color': (255, 150, 100),
        'description': 'Temporary speed boost'
    },
    'burger': {
        'radius': 35,
        'color': (139, 69, 19),
        'points': 30,
        'speed': 0,
        'effect': 'hp_restore',
        'effect_duration': 0,
        'glow_color': (150, 100, 50),
        'description': 'Restores health'
    }
}

# Food effects
food_effects = {
    'speed_boost': {'speed_multiplier': 1.5, 'duration': 500},
    'hp_restore': {'hp_amount': 20},
    'hp_boost': {'hp_amount': 10},
    'none': {'duration': 0}
}

current_food_effect = None
food_effect_timer = 0

# Obstacles
obstacles = []

# Initialize game
spawn_animations = []
particles = []

# Draw functions
def draw_menu():
    screen.fill(LIGHT_GREY)
   
    # Draw title
    title_text = large_font.render("Supermarket Hole.io", True, GOLD)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)
   
    # Draw description
    desc_text = font.render("Collect food, avoid obstacles, grow as big as you can!", True, BLACK)
    desc_rect = desc_text.get_rect(center=(WINDOW_WIDTH // 2, 200))
    screen.blit(desc_text, desc_rect)
   
    # Draw controls
    controls_text = font.render("Controls: Move with mouse | R to reset | P to pause | ESC to quit", True, BLACK)
    controls_rect = controls_text.get_rect(center=(WINDOW_WIDTH // 2, 250))
    screen.blit(controls_text, controls_rect)
   
    # Draw buttons
    start_button.draw(screen)
    quit_button.draw(screen)
   
    pygame.display.flip()

def draw_character_menu():
    screen.fill(LIGHT_GREY)
   
    # Draw title
    title_text = large_font.render("Select Your Character", True, GOLD)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)
   
    # Draw character buttons
    for button in character_buttons:
        button.draw(screen)
   
    # Draw back button
    back_button = MenuButton("Back", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100))
    back_button.draw(screen)
   
    pygame.display.flip()

def draw_game():
    # Update camera position
    camera_pos[0] = -hole_pos[0] + WINDOW_WIDTH // 2
    camera_pos[1] = -hole_pos[1] + WINDOW_HEIGHT // 2
   
    # Draw background
    screen.fill(LIGHT_GREY)
   
    # Draw map tiles
    for (x, y) in map_tiles:
        tile_x = x * TILE_SIZE
        tile_y = y * TILE_SIZE
        pygame.draw.rect(screen, map_tiles[(x, y)]['color'],
                        (tile_x + camera_pos[0], tile_y + camera_pos[1],
                         TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(screen, WHITE,
                        (tile_x + camera_pos[0], tile_y + camera_pos[1],
                         TILE_SIZE, TILE_SIZE), 1)
   
    # Draw food
    for food in food_list:
        pygame.draw.circle(screen, food['color'],
                         (int(food['x'] + camera_pos[0]),
                          int(food['y'] + camera_pos[1])),
                         int(food['radius']))
   
    # Draw hole
    for i in range(int(hole_radius // 2)):
        color = (0, 0, max(0, 255 - (i * 255 // int(hole_radius))))
        pygame.draw.circle(screen, color,
                         (int(WINDOW_WIDTH // 2), int(WINDOW_HEIGHT // 2)),
                         int(hole_radius - i))
   
    # Draw UI
    score_text = font.render(f'Score: {score}', True, BLACK)
    size_text = font.render(f'Size: {int(hole_radius)}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(size_text, (10, 50))
   
    # Draw health bar
    pygame.draw.rect(screen, DARK_GREY, (10, WINDOW_HEIGHT - 50, 200, 30))
    health_width = (hp / max_hp) * 200
    pygame.draw.rect(screen, RED, (10, WINDOW_HEIGHT - 50, health_width, 30))
    pygame.draw.rect(screen, WHITE, (10, WINDOW_HEIGHT - 50, 200, 30), 2)
   
    pygame.display.flip()

def generate_food():
    # Generate food at random position
    food_type = random.choice(list(food_types.keys()))
    food_data = food_types[food_type]
   
    # Generate position away from hole
    while True:
        x = random.randint(-MAP_SIZE, MAP_SIZE)
        y = random.randint(-MAP_SIZE, MAP_SIZE)
        distance = math.sqrt((x - hole_pos[0])**2 + (y - hole_pos[1])**2)
        if distance > hole_radius + 50:  # Make sure food isn't too close to hole
            break
   
    return {
        'x': x,
        'y': y,
        'radius': food_data['radius'],
        'color': food_data['color'],
        'points': food_data['points'],
        'effect': food_data['effect'],
        'effect_duration': food_data['effect_duration']
    }

def check_collision(food):
    global hole_radius, score, hp, max_hp, current_food_effect, food_effect_timer
   
    # Calculate distance between hole and food
    dx = food['x'] - hole_pos[0]
    dy = food['y'] - hole_pos[1]
    distance = math.sqrt(dx**2 + dy**2)
   
    # Check if hole touches food
    if distance < hole_radius + food['radius']:
        # Food is eaten
        hole_radius += 0.5  # Grow hole
        score += food['points']
       
        # Apply food effect if any
        if food['effect'] != 'none':
            current_food_effect = food['effect']
           
            if food['effect'] == 'speed_boost':
                food_effect_timer = food_effects['speed_boost']['duration']
            elif food['effect'] == 'hp_restore':
                hp = min(max_hp, hp + food_effects['hp_restore']['hp_amount'])
            elif food['effect'] == 'hp_boost':
                max_hp = min(200, max_hp + food_effects['hp_boost']['hp_amount'])
                hp = min(hp, max_hp)  # Ensure hp doesn't exceed new max_hp
       
        return True
    return False

def update_food_effects():
    global current_food_effect, food_effect_timer, CAMERA_SPEED
   
    if current_food_effect and food_effect_timer > 0:
        if current_food_effect == 'speed_boost':
            CAMERA_SPEED = 5 * food_effects['speed_boost']['speed_multiplier']
        food_effect_timer -= 1
    else:
        CAMERA_SPEED = 5
        current_food_effect = None

def print_menu(options):
    """Print menu options with numbers."""
    print("\n=== MENU ===")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    print("0. Exit")

def get_user_choice(max_choice):
    """Get and validate user input."""
    while True:
        try:
            choice = input("\nEnter your choice (0-" + str(max_choice) + "): ")
           
            # Handle empty input
            if not choice.strip():
                print("Please enter a number.")
                continue
               
            # Convert to integer
            choice = int(choice)
           
            # Validate range
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 0 and {max_choice}")
        except ValueError:
            print("Please enter a valid number.")

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    mouse_pos = pygame.mouse.get_pos()
   
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if game_state == MENU:
            start_button.update(mouse_pos)
            quit_button.update(mouse_pos)
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.hover:
                    game_state = CHARACTER_MENU
                elif quit_button.hover:
                    running = False
       
        elif game_state == CHARACTER_MENU:
            # Update character buttons
            for button in character_buttons:
                button.update(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN and button.hover:
                    selected_character = button.character
                    # Set character attributes
                    hole_radius = selected_character['radius']
                    max_hp = selected_character['hp']
                    hp = max_hp
                    CAMERA_SPEED = selected_character['speed']
                    game_state = PLAYING
                    score = 0
                    food_list.clear()
                    particles.clear()
                    obstacles.clear()
           
            # Handle back button
            back_button = MenuButton("Back", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100))
            back_button.update(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.hover:
                game_state = MENU
       
        elif game_state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:  # Reset game
                    game_state = CHARACTER_MENU
                    selected_character = None
                    hole_radius = 30
                    hp = 100
                    score = 0
                    food_list.clear()
                    particles.clear()
                    obstacles.clear()
                elif event.key == pygame.K_p:  # Pause game
                    paused = True
                    while paused:
                        for pause_event in pygame.event.get():
                            if pause_event.type == pygame.QUIT:
                                running = False
                                paused = False
                            elif pause_event.type == pygame.KEYDOWN:
                                if pause_event.key == pygame.K_p:
                                    paused = False
                        screen.fill(LIGHT_GREY)
                        pause_text = large_font.render("PAUSED", True, BLACK)
                        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                        screen.blit(pause_text, pause_rect)
                        pygame.display.flip()
                        clock.tick(60)

    # Update game state
    if game_state == MENU:
        draw_menu()
    elif game_state == CHARACTER_MENU:
        draw_character_menu()
    elif game_state == PLAYING:
        # Update food effects
        update_food_effects()
       
        # Move hole towards mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - WINDOW_WIDTH // 2
        dy = mouse_y - WINDOW_HEIGHT // 2
        distance = math.sqrt(dx**2 + dy**2)
       
        if distance > 0:
            speed = min(10, max(5, 15 - hole_radius / 20))
            if distance < 100:
                speed *= 0.8
            hole_pos[0] += dx * speed / distance
            hole_pos[1] += dy * speed / distance
       
        # Generate new food
        if food_cooldown == 0:
            food = generate_food()
            if food:
                food_list.append(food)
                food_cooldown = FOOD_COOLDOWN
        else:
            food_cooldown -= 1
       
        # Check collisions
        new_food_list = []
        for food in food_list:
            if not check_collision(food):
                new_food_list.append(food)
        food_list = new_food_list
       
        # Check if player is dead (hp <= 0)
        if hp <= 0:
            game_state = CHARACTER_MENU
            selected_character = None
            hole_radius = 30
            hp = 100
            score = 0
            food_list.clear()
            particles.clear()
            obstacles.clear()
       
        draw_game()
       
    clock.tick(60)

pygame.quit()