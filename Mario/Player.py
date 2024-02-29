from Personage import Personage
from Visualization import *

mario_left = [
    pygame.image.load("Mario_Anims/mario_left/left1.png"),
    pygame.image.load("Mario_Anims/mario_left/left2.png"),
    pygame.image.load("Mario_Anims/mario_left/left3.png"),
    pygame.image.load("Mario_Anims/mario_left/left4.png"),
    pygame.image.load("Mario_Anims/mario_left/left5.png")
]

mario_right = [
    pygame.image.load("Mario_Anims/mario_right/mright1.png"),
    pygame.image.load("Mario_Anims/mario_right/mright2.png"),
    pygame.image.load("Mario_Anims/mario_right/mright3.png"),
    pygame.image.load("Mario_Anims/mario_right/mright4.png"),
    pygame.image.load("Mario_Anims/mario_right/mright5.png")
]


class Player(Personage):
    def __init__(self):
        super().__init__(pygame.image.load("Mario_Anims/mario_right/mright1.png"))
        self.respawn()
        self.is_jumping = False
        self.jump_count = 11
        self.anim_timer = 0
        self.anim_delay = 70  # Затримка між кадрами анімації (у мілісекундах)
        self.current_frame = 0

    def handle_input(self):
        self.x_speed = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_speed = -self.speed
            self.animate(mario_left)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_speed = self.speed
            self.animate(mario_right)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > W:
            self.rect.right = W

    def jump(self):
        if self.is_grounded:
            self.image = pygame.image.load("Mario_Anims/mario_jump/jump1.png")
            vol = pygame.mixer.Sound("sound/Jump.ogg")
            vol.play()
            self.is_grounded = False
            self.is_jumping = True
            self.jump_count = 11
            self.y_speed = self.jump_speed

    def animate(self, frames):
        now = pygame.time.get_ticks()

        if now - self.anim_timer > self.anim_delay:
            self.anim_timer = now
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.image = frames[self.current_frame]

    def respawn(self):
        self.image = pygame.image.load("Mario_Anims/mario_right/mright1.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (W // 2, H - ground_H)
        self.x_speed = 0
        self.y_speed = 0
        self.is_out = False
        self.is_dead = False
        self.is_grounded = False
