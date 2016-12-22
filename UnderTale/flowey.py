import main_state

from pico2d import *


class Flowey:
    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 2.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None

    STAND, TALK = 0, 1
    START_ROOM, BLACK_ROOM = 0, 1

    def __init__(self):
        self.x, self.y = 400, 300
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = self.STAND
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.scale = 2.0
        self.state = self.STAND
        self.spot = self.BLACK_ROOM
        self.bRoomChange = False

        if Flowey.image == None:
            Flowey.image = load_image('Resource/spr_flowey.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Flowey.RUN_SPEED_PPS * frame_time
        self.total_frames += Flowey.FRAMES_PER_ACTION * Flowey.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        

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
        
        if self.state == self.STAND:
            self.image.clip_draw(clamp(0, self.frame, 0) * 21, 0, 21, self.image.h, self.x, self.y, self.image.w / 2 * self.scale, self.image.h * self.scale)
        elif self.state == self.TALK:
            self.image.clip_draw(clamp(0, self.frame, 1) * 21, 0, 21, self.image.h, self.x, self.y, self.image.w / 2 * self.scale, self.image.h * self.scale)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            pass

        if event.type == SDL_KEYUP:
            pass
