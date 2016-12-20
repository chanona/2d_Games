from pico2d import *

import game_framework


from frisk import Frisk # import Boy class from boy.py
from background import Background


name = "main_state"

pFrisk = None
pBackGround = None

def create_world():
    global pFrisk, pBackGround
    pFrisk = Frisk()
    pBackGround = Background()

    pBackGround.set_center_object(pFrisk)
    pFrisk.set_background(pBackGround)


def destroy_world():
    global pFrisk, pBackGround
    del(pFrisk)
    del(pBackGround)


def enter():
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pFrisk.handle_event(event)
                pBackGround.handle_event(event)



def update(frame_time):
    pFrisk.update(frame_time)
    pBackGround.update(frame_time)



def draw(frame_time):
    clear_canvas()
    pBackGround.draw()
    pFrisk.draw()
    update_canvas()






