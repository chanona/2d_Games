import main_state

from pico2d import *


class Floweybullet:
    image = None
    Floweyimage = None

    PIXEL_PER_METER = (10.0 / 2.0)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7
         
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.destx, self.desty = 0, 0
        self.scale = 1.0
        self.floweyframe = 0
        self.Totalfloweyframe = 0
        self.bAlive = False
        self.player = None
        self.flowey = None
        self.bStart = False


        if Floweybullet.image == None:
            Floweybullet.image = load_image('Resource/flowey_bullet.png')

    def update(self, frame_time):
        self.Totalfloweyframe += Floweybullet.FRAMES_PER_ACTION * Floweybullet.ACTION_PER_TIME * frame_time
        self.floweyframe = int(self.Totalfloweyframe) % 2
        distance = Floweybullet.RUN_SPEED_PPS * frame_time

        if self.flowey.bBattleStart == True:
            if self.x > self.player.x:
                self.x -= (distance) / 2
            elif self.x < self.player.x:
                self.x += (distance) / 2
            self.y -= distance
        
    def move(self, x, y):
        self.destx = x, self.desty = y   

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.bAlive = False

    def set_player(self, player):
        self.player = player
    
    def set_flowey(self, flowey):
        self.flowey = flowey
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        global image
        self.image.clip_draw(clamp(0, self.floweyframe, 1) * 22, 0, 22, self.image.h, self.x, self.y, self.image.w / 2 * self.scale, self.image.h * self.scale)
        
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            pass

                
                
