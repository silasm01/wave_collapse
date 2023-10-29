import pygame, os
from world import World
from player import Player

pygame.font.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.state = "menu"
        self.world = None
        self.player = Player()
        self.textures = {}
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("jetbrainsmonoregular", 20)
        for image in os.listdir("img/"):
            self.textures[image.split(".")[0]] = pygame.image.load("img/"+image)

    def load_world(self, name):
        with open("worlds/"+name+".json", "r") as f:
            self.world = f.read()

    def run(self):
        self.world = World("test", self.textures)
        while self.state:
            self.handle_events()
            self.render(self.world)
            dt = self.clock.tick()/1000
            fps = self.font.render(str(dt), False, (255,255,255))
            self.screen.blit(fps,(0,0))
            pos = self.font.render(str(self.player.position), False, (255,255,255))
            self.screen.blit(pos,(0,30))
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = False

        dt = self.clock.tick()/1000*60
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
           self.player.position[1] += 10*dt
        if keys[pygame.K_s]:
           self.player.position[1] -= 10*dt
        if keys[pygame.K_a]:
           self.player.position[0] += 10*dt
        if keys[pygame.K_d]:
           self.player.position[0] -= 10*dt




    def render(self, world):
        self.screen.fill((0,0,0))
        for tile in self.world.tiles:
            self.screen.blit(self.world.textures[tile["image"]],(tile["position"][0]*32+self.screen.get_size()[0]/2+self.player.position[0],tile["position"][1]*32+self.screen.get_size()[1]/2+self.player.position[1]))
