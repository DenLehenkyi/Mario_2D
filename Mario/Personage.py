from Visualization import *


class Personage:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 3
        self.is_out = False
        self.is_dead = False
        self.jump_speed = -12
        self.gravity = 0.5
        self.is_grounded = False

    def handle_input(self):
        pass

    def kill(self, dead_image):
        self.image = dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed

    def update(self):
        self.rect.x += self.x_speed
        self.y_speed += self.gravity
        self.rect.y += self.y_speed

        if self.is_dead:
            if self.rect.top > H - ground_H:
                self.is_out = True
        else:
            self.handle_input()

            if self.rect.bottom > H - ground_H:
                self.is_grounded = True
                self.y_speed = 0
                self.rect.bottom = H - ground_H

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def animate(self):
        pass

    def spawn(self):
        pass
