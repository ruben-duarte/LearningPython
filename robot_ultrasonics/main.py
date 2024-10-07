import math
import pygame


from robot_car import Graphics, Robot, Ultrasonic



MAP_DIMENSIONS = (600, 1200)


gfx = Graphics(MAP_DIMENSIONS,'car1.png', 'map.png')
WINDOW = pygame.display.set_mode((1200,600))
WINDOW.fill((0,0,0))

# robot
start = (900,200)
robot = Robot(start, 0.01*3779.52)

#sensor
sensor_range = 250, math.radians(40)
ultra_sonic = Ultrasonic(sensor_range,gfx.map)

delta_t = 0
last_time = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_t = (pygame.time.get_ticks() - last_time) / 1000
    last_time = pygame.time.get_ticks()

    gfx.map.blit(gfx.map_img,(0,0))

    robot.kinematics(delta_t)
    gfx.draw_robot(robot.x, robot.y, robot.heading)
    point_cloud = ultra_sonic.sense_obstacles(robot.x,robot.y, robot.heading)
    robot.avoid_obstacles(point_cloud, delta_t)
    gfx.draw_sensor_data(point_cloud)
    
    

    pygame.display.update()
