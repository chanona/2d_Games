import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import pico2d
import game_framework

import main_state
import title_state

pico2d.open_canvas()
game_framework.run(title_state)
pico2d.close_canvas()
