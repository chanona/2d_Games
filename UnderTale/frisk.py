import random
import main_state

from pico2d import *


class Frisk:
    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None

    DOWN_STAND, DOWN_RUN, LEFT_STAND, LEFT_RUN, RIGHT_STAND, RIGHT_RUN, UP_STAND, UP_RUN = 0,1,2,3,4,5,6,7
    START_ROOM, BLACK_ROOM, BATTLE_ROOM = 0, 1, 2
    NONE, BLACKROOM_FLOWEY = 0, 1
    NONE, BT_FLOWEY = 0, 1

    def __init__(self):
        self.x, self.y = 430, 360
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = self.UP_STAND
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.scale = 2.0
        self.state = self.UP_STAND
        self.playerspot = self.START_ROOM
        self.bRoomChange = False
        self.talkevent = self.NONE
        self.bBattle = False
        self.BattleState = self.NONE

        if Frisk.image == None:
            Frisk.image = load_image('Resource/Frisk_Animation.png')


    def set_background(self, bg):
        self.bg = bg

    def set_talkwindow(self, tw):
        self.tw = tw

    def update(self, frame_time):
        if self.talkevent == self.NONE:
            self.life_time += frame_time
            distance = Frisk.RUN_SPEED_PPS * frame_time
            self.total_frames += Frisk.FRAMES_PER_ACTION * Frisk.ACTION_PER_TIME * frame_time
            self.frame = int(self.total_frames) % 10
            self.x += (self.xdir * distance)
            self.y += (self.ydir * distance)

            self.x = clamp(0, self.x, self.bg.w)
            self.y = clamp(0, self.y, self.bg.h)


        if self.xdir == -1: self.state = self.LEFT_RUN
        elif self.xdir == 1: self.state = self.RIGHT_RUN
        elif self.ydir == -1: self.state = self.DOWN_RUN
        elif self.ydir == 1: self.state = self.UP_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN: self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN: self.state = self.LEFT_STAND
            elif self.state == self.DOWN_RUN: self.state = self.DOWN_STAND
            elif self.state == self.UP_RUN: self.state = self.UP_STAND

        if self.playerspot == self.START_ROOM and self.x >= 1800 and self.x <= 1908 and self.y >= 345 and self.y <= 347:
            self.playerspot = self.BLACK_ROOM
            self.bRoomChange = True
            self.x = 400
            self.y = 50
        
        if self.playerspot == self.BLACK_ROOM and self.y >= 200 and self.tw.Floweytalkcnt <= 9:
            self.talkevent = self.BLACKROOM_FLOWEY
        else:
            if self.talkevent == self.BLACKROOM_FLOWEY and self.BattleState == self.NONE:
                self.BattleState = self.BT_FLOWEY
                self.talkevent = self.NONE
            
    def draw(self):
        # x_left_offset = min(0, self.x - self.canvas_width//2)
        # x_right_offset = max(0, self.x - self.bg.w + self.canvas_width//2)
        # x_offset = x_left_offset + x_right_offset
        # self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.canvas_width//2+x_offset, self.canvas_height//2)
        # debug_print('x=%d, y=%d, x_left_offset=%d, x_right_offset=%d' % (self.x, self.y, x_left_offset, x_right_offset))

        # x, y : map coord
        # sx, sy : screen coord
        # screen_origin_x : map coord x of screen_origin
        # screen_origin_y : map coord y of screen_origin
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        #debug_print('x=%d, y=%d, sx=%d, sy=%d' % (self.x, self.y, sx, sy), 0, 255, 0)

        # 이동
        if self.state == self.RIGHT_STAND:
            self.image.clip_draw(clamp(5, self.frame, 5) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.RIGHT_RUN:
            self.image.clip_draw(clamp(5, self.frame, 6) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.LEFT_STAND:
            self.image.clip_draw(clamp(3, self.frame, 3) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.LEFT_RUN:
            self.image.clip_draw(clamp(3, self.frame, 4) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.UP_STAND:
            self.image.clip_draw(clamp(7, self.frame, 7) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.UP_RUN:
            self.image.clip_draw(clamp(8, self.frame, 9) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)
        elif self.state == self.DOWN_STAND:
            self.image.clip_draw(clamp(0, self.frame, 0) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale)    
        elif self.state == self.DOWN_RUN:
            self.image.clip_draw(clamp(1, self.frame, 2) * 20, 0, 20, self.image.h, sx, sy, self.image.w / 10 * self.scale, self.image.h * self.scale) 

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        if self.talkevent == self.NONE:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT: self.xdir += -1
                elif event.key == SDLK_RIGHT: self.xdir += 1
                elif event.key == SDLK_UP: self.ydir += 1
                elif event.key == SDLK_DOWN: self.ydir -= 1

            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT: self.xdir += 1
                elif event.key == SDLK_RIGHT: self.xdir -= 1
                elif event.key == SDLK_UP: self.ydir -= 1
                elif event.key == SDLK_DOWN: self.ydir += 1
        else:
            if self.state == self.RIGHT_RUN: 
                self.xdir -= 1
            elif self.state == self.LEFT_RUN: 
                self.xdir += 1
            elif self.state == self.DOWN_RUN: 
                self.ydir += 1
            elif self.state == self.UP_RUN: 
                self.ydir -= 1
