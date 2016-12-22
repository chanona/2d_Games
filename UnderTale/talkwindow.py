import main_state

from pico2d import *


class TalkWindow:
    image = None
    Floweyimage = None

    TIME_PER_ACTION = 2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    def __init__(self):
        self.x, self.y = 400, 300
        self.scale = 2.0
        self.Line1, self.Line2, self.Line3 = 1, 0, 0
        self.font = load_font('ConsolaMalgun.TTF')
        self.black_flowey_str = [' ', '* Howdy!!', '* Im FLOWEY.', '* FLOWEY the FLOWER !',
                                 '* Hmmm...', 
                                 '* Youre new to the', '  UNDERGROUND, arentcha?',
                                 '* Golly, you must be' ,'  so confused.',
                                 '* Someone ought to teach' , '  you how things work', '  around here!',
                                 '* I guess little old me', '  will have to do.',
                                 '* Ready?' , '* Here we go!']

        self.Floweytalkcnt = 1 
        self.floweyframe = 0
        self.Totalfloweyframe = 0
        self.bgm = load_music('Resource//mus_flowey.ogg')
                
        if TalkWindow.image == None:
            TalkWindow.image = load_image('Resource/spr_talkwindow_0.png')

        if TalkWindow.Floweyimage == None:
            TalkWindow.Floweyimage = load_image('Resource/Flowey_talk.png')

    def update(self, frame_time):
        self.Totalfloweyframe += TalkWindow.FRAMES_PER_ACTION * TalkWindow.ACTION_PER_TIME * frame_time
        self.floweyframe = int(self.Totalfloweyframe) % 2

    def set_player(self, player):
        self.player = player

    def draw(self):
        global image
        self.image.draw(400, 480, 680, 180)
        
        self.font.draw(165, 530, self.black_flowey_str[self.Line1], (255, 255, 255))
        self.font.draw(165, 500, self.black_flowey_str[self.Line2], (255, 255, 255))
        self.font.draw(165, 470, self.black_flowey_str[self.Line3], (255, 255, 255))
        self.Floweyimage.clip_draw(clamp(0, self.floweyframe, 1) * 42, 0, 42, self.Floweyimage.h, 120, 480, self.Floweyimage.w / 2 * self.scale, self.Floweyimage.h * self.scale)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            pass

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.player.talkevent == self.player.BLACKROOM_FLOWEY:
                if self.Floweytalkcnt == 0:
                    self.Line1, self.Line2, self.Line3 = 1,0,0
                elif self.Floweytalkcnt == 1:
                    self.Line1, self.Line2, self.Line3 = 1,2,0
                    self.bgm.set_volume(64)
                    self.bgm.repeat_play()
                elif self.Floweytalkcnt == 2:
                    self.Line1, self.Line2, self.Line3 = 1,2,3
                elif self.Floweytalkcnt == 3:
                    self.Line1, self.Line2, self.Line3 = 4,0,0
                elif self.Floweytalkcnt == 4:
                    self.Line1, self.Line2, self.Line3 = 5,6,0
                elif self.Floweytalkcnt == 5:
                    self.Line1, self.Line2, self.Line3 = 7,8,0
                elif self.Floweytalkcnt == 6:
                    self.Line1, self.Line2, self.Line3 = 9,10,11
                elif self.Floweytalkcnt == 7:
                    self.Line1, self.Line2, self.Line3 = 12,13,0
                elif self.Floweytalkcnt == 8:
                    self.Line1, self.Line2, self.Line3 = 14,0,0
                elif self.Floweytalkcnt == 9:
                    self.Line1, self.Line2, self.Line3 = 14,15,0
                
            self.Floweytalkcnt +=1
                                  
                
                
