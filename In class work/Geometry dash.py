import pygame as py
import random

py.init()

SETTINGS = {
    "screen_width": 800,
    "screen_height": 400,
    "fps": 60,
    "gravity": 0.8,
    "jump_strength": -15,
    "bg_color": (30, 30, 30),
    "player_color": (0, 255, 255),
    "obstacle_color": (255, 50, 50)
}

def check_collision(player_rect, obstacles):

    for obs in obstacles:
        if player_rect.colliderect(obs):
            return True
    return False

def run_game():
    py.init()
    screen = py.display.set_mode((SETTINGS["screen_width"], SETTINGS["screen_height"]))
    clock = py.time.Clock()

    player_rect = py.Rect(100, 300, 40, 40)
    player_vel_y = 0
    is_jumping = False
    
    # Obstacles - A list to store multiple obstacle objects
    obstacles = []
    spawn_timer = 0
    
    score = 0
    running = True

    while running:
        screen.fill(SETTINGS["bg_color"])
        
        # 1. Event Handling
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE and not is_jumping:
                    player_vel_y = SETTINGS["jump_strength"]
                    is_jumping = True

        # 2. Physics & Movement
        player_vel_y += SETTINGS["gravity"]
        player_rect.y += player_vel_y

        # Floor Collision
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
            is_jumping = False

        # 3. Obstacle Logic
        spawn_timer += 1
        if spawn_timer > 60:  # Spawn every ~1 second
            new_obs = py.Rect(800, 310, 30, 40)
            obstacles.append(new_obs)
            spawn_timer = 0

        for obs in obstacles[:]: # Iterate over a copy to allow removal
            obs.x -= 7 # Move left
            if obs.right < 0:
                obstacles.remove(obs)
                score += 1
            py.draw.rect(screen, SETTINGS["obstacle_color"], obs)

        # 4. Collision Check (Using our custom function)
        if check_collision(player_rect, obstacles):
            print(f"Game Over! Final Score: {score}")
            running = False

        # 5. Drawing
        py.draw.rect(screen, SETTINGS["player_color"], player_rect)
        py.draw.line(screen, (255, 255, 255), (0, 350), (800, 350), 2) # Ground
        
        py.display.flip()
        clock.tick(SETTINGS["fps"])

    py.quit()

if __name__ == "__main__":
    run_game()

