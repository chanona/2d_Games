from pico2d import *

import game_framework


from frisk import Frisk # import Boy class from boy.py
from background import Background, BlackRoom, BattleRoom
from flowey import Flowey
from talkwindow import TalkWindow
from friskheart import FriskHeart
from battleflowey import Battleflowey
from floweybullet import Floweybullet

name = "main_state"

pFrisk = None
pStartRoom = None
pBlackRoom = None
pFlowey = None
pTalkWindow = None
pFriskHeart = None
pBattleRoom = None
pbattleflowey = None
listFloweybullet = None
pFloweybullet1, pFloweybullet2, pFloweybullet3, pFloweybullet4, pFloweybullet5 = None,None,None,None,None

def create_world():
    global pFrisk, pStartRoom, pBlackRoom, pFlowey, pTalkWindow, pFriskHeart, pBattleRoom, pbattleflowey, listFloweybullet
    global pFloweybullet1, pFloweybullet2, pFloweybullet3, pFloweybullet4, pFloweybullet5
    pFrisk = Frisk()
    pStartRoom = Background()
    pBlackRoom = BlackRoom()
    pFlowey = Flowey()
    pTalkWindow = TalkWindow()
    pFriskHeart = FriskHeart()
    pBattleRoom = BattleRoom()
    pbattleflowey = Battleflowey()
    pFloweybullet1, pFloweybullet2, pFloweybullet3, pFloweybullet4, pFloweybullet5 = Floweybullet(200, 460),Floweybullet(300, 500),Floweybullet(400, 540),Floweybullet(500, 500), Floweybullet(600, 460)
    listFloweybullet = [pFloweybullet1, pFloweybullet2, pFloweybullet3, pFloweybullet4, pFloweybullet5]

    pStartRoom.set_center_object(pFrisk)
    pFrisk.set_background(pStartRoom)
    pFrisk.set_talkwindow(pTalkWindow)
    pTalkWindow.set_player(pFrisk)

def change_room(bg):
    bg.set_center_object(pFrisk)
    pFrisk.set_background(bg)
    pFrisk.bRoomChange = False

def destroy_world():
    global pFrisk, pStartRoom, pBlackRoom, pFlowey, pTalkWindow, pFriskHeart, pBattleRoom, pbattleflowey
    del(pFrisk)
    del(pStartRoom)
    del(pBlackRoom)
    del(pFlowey)
    del(pTalkWindow)
    del(pFriskHeart)
    del(pBattleRoom)
    del(pbattleflowey)

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
            elif pFrisk.BattleState == pFrisk.NONE:
                pFrisk.handle_event(event)
                if pFrisk.playerspot == pFrisk.START_ROOM:
                    pStartRoom.handle_event(event)
                if pFrisk.playerspot == pFrisk.BLACK_ROOM:
                    pBlackRoom.handle_event(event)
                    pFlowey.handle_event(event)
                    if pFrisk.talkevent == pFrisk.BLACKROOM_FLOWEY:
                        pTalkWindow.handle_event(event)
            else:
                pFriskHeart.handle_event(event)
                pbattleflowey.handle_event(event)
                
def update(frame_time):
    pFrisk.update(frame_time)

    if pFrisk.bRoomChange == True:
        if pFrisk.playerspot == pFrisk.START_ROOM:
            change_room(pStartRoom)
        if pFrisk.playerspot == pFrisk.BLACK_ROOM:
            change_room(pBlackRoom)

    if pFrisk.playerspot == pFrisk.START_ROOM:
        pStartRoom.update(frame_time)
    elif pFrisk.playerspot == pFrisk.BLACK_ROOM:
        pBlackRoom.update(frame_time)
        pFlowey.update(frame_time)
        if pFrisk.talkevent == pFrisk.BLACKROOM_FLOWEY:
            pTalkWindow.update(frame_time)
            pFlowey.state = pFlowey.TALK
                
    if pFrisk.BattleState != pFrisk.NONE:
        pFriskHeart.update(frame_time)
        pBattleRoom.update(frame_time)
        pbattleflowey.update(frame_time)
        for bullet in listFloweybullet:
            bullet.update(frame_time)
     
def draw(frame_time):
    clear_canvas()

    if pFrisk.BattleState == pFrisk.NONE:
        if pFrisk.playerspot == pFrisk.START_ROOM:
            pStartRoom.draw()
        elif pFrisk.playerspot == pFrisk.BLACK_ROOM:
            pBlackRoom.draw()
            pFlowey.draw()
            if pFrisk.talkevent != pFrisk.NONE:
                pTalkWindow.draw()
        pFrisk.draw()
    else:
        pBattleRoom.draw()
        pFriskHeart.draw()
        pbattleflowey.draw()
        for bullet in listFloweybullet:
            bullet.draw()
    update_canvas()






