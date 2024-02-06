import pygame as pg
from config import *
import random

pg.init()
running = True
display = pg.display.set_mode((600, 800))

Road = pg.image.load('photos/road.png')
Oversized_car = pg.image.load('photos/car.png')
Oversized_civilian_car = pg.image.load('photos/civilian_car.png')
Oversized_civilian_car2 = pg.image.load('photos/civilian_car2.png')
oversized_dashboard = pg.image.load('photos/dashboard.png')
oversized_dashboard_pointer = pg.image.load('photos/dashboard_metermeter.png')

Car = pg.transform.scale(Oversized_car, (600, 600))

civilian_car = pg.transform.scale(Oversized_civilian_car, (175, 175))
civilian_car2 = pg.transform.scale(Oversized_civilian_car2, (175, 175))

dashboard = pg.transform.scale(oversized_dashboard, (300, 300))
dashboard_pointer = pg.transform.scale(oversized_dashboard_pointer, (300, 300))

velocity = 0
travel_lenght = 0
x = 255
display.fill((0, 0, 0))
pg.display.set_caption("Deeplearning Drag-racing")
surrounding = 0
civilian_cars = []
angle = -180
roads = [301, 401, 501, 601]
crash_counter = 0


# Pygame update function
def update():
    pg.display.update()
    display.fill((0, 0, 0))


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        exit("Program stopped, cause: User pressed escape.")

    if not ai_play:
        if keys[pg.K_w] or keys[pg.K_UP]:
            velocity += acceleration_speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            if velocity >= 0.2:
                velocity -= brake_speed
        if keys[pg.K_a] and x >= 105 or keys[pg.K_LEFT] and x >= 105:
            x -= velocity * steering_speed

        if keys[pg.K_d] and x <= 405 or keys[pg.K_RIGHT] and x <= 405:
            x += velocity * steering_speed

    surrounding += velocity
    travel_lenght += velocity

    if surrounding >= 800:
        surrounding = 0

    if len(civilian_cars) < 3:
        color = random.randint(1, 2)
        road = random.choice(roads)
        speed = random.uniform(0.20, 0.85)
        civilian_cars.append({"color": color, "road": road, "y": -165, "speed": speed})

    # drawing on screen
    display.blit(Road, (0, surrounding - 800))
    display.blit(Road, (0, surrounding))

    display.blit(Car, (x - 240, 200))  # huh? why  -240?
    if hitbox_visuals:
        Car_hitbox = pg.Rect(x, 458, 90, 120)
        pg.draw.rect(display, (255, 0, 0), Car_hitbox, 1)

    for car in civilian_cars:
        color = car["color"]
        road = car["road"]
        y = car["y"]
        speed = car["speed"]
        civilian_car_hitbox = pg.Rect(road - 196, y + 12, 89, 154)
        Car_hitbox = pg.Rect(x, 458, 90, 120)
        if color == 1:
            display.blit(civilian_car, (road - 240, y))
            if hitbox_visuals:
                pg.draw.rect(display, (255, 0, 0), civilian_car_hitbox, 1)
        else:
            display.blit(civilian_car2, (road - 240, y))
            if hitbox_visuals:
                pg.draw.rect(display, (255, 0, 0), civilian_car_hitbox, 1)
        if collision:
            if civilian_car_hitbox.colliderect(Car_hitbox):
                crash_counter += 1

        car["y"] += speed * (velocity - stable_civilian_car_speed)

        if y >= 965:
            civilian_cars.remove(car)

    if speedometer:
        speed_in_degrees = -velocity * 4.5 - 180
        if velocity >= max_speed:
            velocity = max_speed
        elif velocity < 61:
            angle = speed_in_degrees
        elif 61 <= velocity <= 100:
            angle = -random.randint(450, 465)
        elif velocity >= 101:
            if crazy_speedometer:
                angle -= 25
            else:
                angle = -random.randint(450, 465)

        dashboard_pointer_rotated = pg.transform.rotate(dashboard_pointer, angle)
        rect = dashboard_pointer_rotated.get_rect(center=(350 + 150, 550 + 150))

        display.blit(dashboard, (350, 550))
        display.blit(dashboard_pointer_rotated, rect.topleft)
        print("crashes:", crash_counter)
    update()
