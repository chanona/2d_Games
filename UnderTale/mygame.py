import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import pico2d
import game_framework

import scroll_state as main_state

pico2d.open_canvas()
game_framework.run(main_state)
pico2d.close_canvas()
