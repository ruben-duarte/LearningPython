import pygame
import math
import numpy as np

def distance(point_1, point_2):
    point_1 = np.array(point_1)
    point_2 = np.array(point_2)
    return np.linalg.norm(point_1 - point_2)

class Robot:
    def __init__(self,start_position, width):
        self.METERS_TO_PIXELS = 3779.52

        self.width = width
        self.x = start_position[0]
        self.y = start_position[1]
        self.heading = 0
        self.left_velocity = 0.01 * self.METERS_TO_PIXELS
        self.right_velocity = 0.01 * self.METERS_TO_PIXELS
        self.maxspeed = 0.02*self.METERS_TO_PIXELS
        self.minspeed = 0.01*self.METERS_TO_PIXELS
        self.min_obstacle_distance = 100 #pixels
        self.count_down = 5 #secs
    
    def avoid_obstacles(self,point_cloud,delta_t):
        closest_obstacle = None
        dist = np.inf

        if len(point_cloud) > 1:
            for point in point_cloud:
                if dist > distance([self.x,self.y],point):
                    dist = distance([self.x,self.y],point)
                    closest_obstacle = (point,dist)
            print(f"Closest obstacle distance: {dist}")
            
            if closest_obstacle[1] < self.min_obstacle_distance and self.count_down > 0:
                self.count_down -= delta_t
                print(f"Count down after moving backward: {self.count_down}")
                self.move_backward()
            else:
                self.count_down = 5
                self.move_forward()

    def move_backward(self):
        print("Moving backward")
        self.right_velocity = - self.minspeed
        self.left_velocity = - self.minspeed/2

    def move_forward(self):
        print("Moving forward")
        self.right_velocity = self.minspeed
        self.left_velocity = self.minspeed

    def kinematics(self, delta_t):
        self.x += ((self.left_velocity + self.right_velocity)/2) * math.cos(self.heading) * delta_t
        self.y -= ((self.left_velocity + self.right_velocity)/2) * math.sin(self.heading) * delta_t
        self.heading += (self.right_velocity - self.left_velocity) / self.width * delta_t

        print(f"Position: ({self.x}, {self.y}), Heading: {self.heading}")
        print(f"Left Velocity: {self.left_velocity}, Right Velocity: {self.right_velocity}")
        if self.heading > 2*math.pi or self.heading < -2*math.pi:
            self.heading = 0
        
        self.right_velocity = max(min(self.maxspeed,self.right_velocity),self.minspeed)
        self.left_velocity = max(min(self.maxspeed,self.right_velocity),self.minspeed)

class Graphics:
    def __init__(self, dimentions,robot_img_path, map_img_path):
        pygame.init()
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.yellow = (255,255,0)

        #loading images
        self.robot = pygame.image.load(robot_img_path)
        self.map_img = pygame.image.load(map_img_path)
        self.height, self.width = dimentions
        #reduce size image
        original_width, original_height = self.robot.get_size()
        new_width, new_height = original_width // 3, original_height // 3
        self.robot = pygame.transform.scale(self.robot, (new_width, new_height))
        #window settings
        pygame.display.set_caption("Obstacle avoidance")
        self.map = pygame.display.set_mode((self.width,self.height))
        self.map.blit(self.map_img,(0,0))

    def draw_robot(self,x,y,heading):
        rotated = pygame.transform.rotozoom(self.robot, math.degrees(heading),1)
        rect = rotated.get_rect(center=(x,y))
        self.map.blit(rotated,rect)

    def draw_sensor_data(self, point_cloud):
        for point in point_cloud:
            pygame.draw.circle(self.map,self.green,point,3,0)

class Ultrasonic:
    def __init__(self, sensor_range,map):
        self.sensor_range = sensor_range
        self.map_width, self.map_height = pygame.display.get_surface().get_size()
        self.map = map
    
    def sense_obstacles(self,x,y,heading):
        obstacles = []
        x1,y1 = x,y
        start_angle = heading - self.sensor_range[1]
        finish_angle = heading + self.sensor_range[1]
        for angle in np.linspace(start_angle, finish_angle,20,False):
            x2 = x1 + self.sensor_range[0] * math.cos(angle)
            y2 = y1 - self.sensor_range[0] * math.sin(angle)
            for i in range(0,100):
                u = i/100
                x = int(x2 * u + x1 * (1-u))
                y = int(y2 * u + y1 * (1-u))
                if 0 < x < self.map_width and 0 < y < self.map_height:
                    color = self.map.get_at((x,y))
                    self.map.set_at((x,y),(0,200,255))
                    if (color[0], color[1], color[2]) == (0,162,232):
                        obstacles.append([x,y])
                        break
        return obstacles                      
