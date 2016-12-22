import main_state

from pico2d import *


class Floweybullet:
    image = None
    Floweyimage = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7
            
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.destx, self.desty = 0, 0
        self.scale = 1.0
        self.floweyframe = 0
        self.Totalfloweyframe = 0
        self.Alive = False
        self.player = None
        self.flowey = None

        if Floweybullet.image == None:
            Floweybullet.image = load_image('Resource/flowey_bullet.png')

    def update(self, frame_time):
        self.Totalfloweyframe += Floweybullet.FRAMES_PER_ACTION * Floweybullet.ACTION_PER_TIME * frame_time
        self.floweyframe = int(self.Totalfloweyframe) % 2
        
    def move(self, x, y):
        self.destx = x, self.desty = y   

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.Alive = False

    def set_player(self, player):
        self.player = player
    
    def set_flowey(self, flowey):
        self.flowey = flowey

    def draw(self):
        global image
        self.image.clip_draw(clamp(0, self.floweyframe, 1) * 22, 0, 22, self.image.h, self.x, self.y, self.image.w / 2 * self.scale, self.image.h * self.scale)
        
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            pass

                
                
