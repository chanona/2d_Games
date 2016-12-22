import main_state

from pico2d import *


class Battleflowey:
    image = None
    Floweyimage = None

    TIME_PER_ACTION = 2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    FLOWEY_NOMAL, FLOWEY_WINK, FLOWEY_SERIOUS1, FLOWEY_SERIOUS2, FLOWEY_ANGRY = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 400, 350
        self.scale = 2.0
        self.Line1, self.Line2, self.Line3, self.Line4 = 1, 0, 0, 0
        self.font = load_font('ConsolaMalgun.TTF')
        self.black_flowey_str = [' ', 'See that heart?', 'That is your SOUL,', 'the very culmination', 'of your being!',
                                 'Your SOUL stars off', 'weak, but can grow', 'strong if you gain', 'a lot of LV.',
                                 'Whats LV stand for?', 'Why, LOVE, of course!',
                                 'You want some', 'LOVE, dont you?',
                                 'Dont worry,', 'I will share some', 'with you!',
                                 'Down here, LOVE is', 'shared through...',
                                 'Little white...', '"freiendliness', 'pellets."',
                                 'Are you ready?',
                                 'Move around!', 'Get as many as', 'you can!']
        self.state = self.FLOWEY_NOMAL
        self.Floweytalkcnt = 1 
        self.floweyframe = 0
        self.Totalfloweyframe = 0

        if Battleflowey.image == None:
            Battleflowey.image = load_image('Resource/spr_blconwdshrt_0.png')

        if Battleflowey.Floweyimage == None:
            Battleflowey.Floweyimage = load_image('Resource/flowey_battle.png')

    def update(self, frame_time):
        self.Totalfloweyframe += Battleflowey.FRAMES_PER_ACTION * Battleflowey.ACTION_PER_TIME * frame_time
        self.floweyframe = int(self.Totalfloweyframe) % 7

    def set_player(self, player):
        self.player = player

    def draw(self):
        global image
        self.image.draw(600, 350, self.image.w * 1.2, self.image.h * 1.2)
        
        self.font.draw(510, 390, self.black_flowey_str[self.Line1], (0, 0, 0))
        self.font.draw(510, 370, self.black_flowey_str[self.Line2], (0, 0, 0))
        self.font.draw(510, 350, self.black_flowey_str[self.Line3], (0, 0, 0))
        self.font.draw(510, 330, self.black_flowey_str[self.Line4], (0, 0, 0))

        if self.state == self.FLOWEY_NOMAL:
            self.Floweyimage.clip_draw(clamp(0, self.floweyframe, 0) * 42, 0, 42, self.Floweyimage.h, self.x, self.y, self.Floweyimage.w / 7 * self.scale, self.Floweyimage.h * self.scale)
        if self.state == self.FLOWEY_WINK:
            self.Floweyimage.clip_draw(clamp(1, self.floweyframe, 1) * 42, 0, 42, self.Floweyimage.h, self.x, self.y, self.Floweyimage.w / 7 * self.scale, self.Floweyimage.h * self.scale)
        if self.state == self.FLOWEY_SERIOUS1:
            self.Floweyimage.clip_draw(clamp(2, self.floweyframe, 2) * 42, 0, 42, self.Floweyimage.h, self.x, self.y, self.Floweyimage.w / 7 * self.scale, self.Floweyimage.h * self.scale)
        if self.state == self.FLOWEY_SERIOUS2:
            self.Floweyimage.clip_draw(clamp(3, self.floweyframe, 4) * 42, 0, 42, self.Floweyimage.h, self.x, self.y, self.Floweyimage.w / 7 * self.scale, self.Floweyimage.h * self.scale)
        if self.state == self.FLOWEY_ANGRY:
            self.Floweyimage.clip_draw(clamp(5, self.floweyframe, 6) * 42, 0, 42, self.Floweyimage.h, self.x, self.y, self.Floweyimage.w / 7 * self.scale, self.Floweyimage.h * self.scale)
        
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            pass

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.Floweytalkcnt < 9:
                if self.Floweytalkcnt == 0:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 1,2,3,4
                elif self.Floweytalkcnt == 1:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 5,6,7,8
                elif self.Floweytalkcnt == 2:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 9,10,0,0
                elif self.Floweytalkcnt == 3:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 11,12,0,0
                elif self.Floweytalkcnt == 4:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 13,14,15,0 # 11
                    self.state = self.FLOWEY_WINK
                elif self.Floweytalkcnt == 5:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 16,17,0,0 #22
                    self.state = self.FLOWEY_NOMAL
                elif self.Floweytalkcnt == 6:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 18,19,20,0 
                elif self.Floweytalkcnt == 7:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 21,0,0,0
                elif self.Floweytalkcnt == 8:
                    self.Line1, self.Line2, self.Line3, self.Line4 = 22,23,24,0
                self.Floweytalkcnt +=1
                                  
                
                
