from Personage import Personage
from Visualization import *


class Goomba(Personage):
    def __init__(self):
        super().__init__(goomba_skin)
        self.respawn()

    def handle_input(self):
        pass

    def respawn(self):
        self.image = goomba_skin
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (W, H - ground_H)
        self.x_speed = -2
        self.y_speed = 0
        self.is_out = False
        self.is_dead = False
