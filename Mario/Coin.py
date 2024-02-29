from Personage import Personage
from Visualization import *
import random

class Coin(Personage):
    def __init__(self):
        super().__init__(coin)
        self.rect.x = random.randint(0, W - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        # Якщо монета виходить за межі екрану, вона знищується
        if self.rect.y > H:
            self.kill(coin)
