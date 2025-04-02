"""Main game script

Run with CTRL+T (thonny), currently contains game loop setup, utility labels and
interface tests. If _curses module missing, run pip install windows-curses in
terminal.

Contributors:
    Romain
"""

from common import Character, DialogLine, move_toward
import cuinter
import logging
import random
import time

FPS_COUNTER_REFRESH = 1 # Time between each FPS counter update

############ System init

logger = logging.getLogger(__name__)
logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG)

cuinter.start()

last_time = time.time()
fps_timer = last_time  # Time of the last FPS update
frame_count = 0

fps_label = cuinter.Label.new(0, 0)

############ Game constants and variables go here

dialog = (
    DialogLine("LELOLELOELOLEOLEOLEOLEOLEOLOLEOLOEELOmmmmmmmmmmmmmmmmmm    yeseiurrrrrhjsdhdjhsdjhsdhjsdhjdshjsdjhsdjhdsjhdshjsdhjsdhjsdhjdshjdshdsdssjhgfqwè¨qè¨¨èwq¨qwèwq", Character("Idris")),
    DialogLine("bruh"),
    DialogLine("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
    DialogLine("We're no strangers to love You know the rules and so do I A full commitment's what I'm thinkin' of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it Inside, we both know what's been going on We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it Inside, we both know what's been going on We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you", Character("Rick Astley")),
)

options = (
    "haram",
    "harambe",
    "PETAH",
    "The honse is here.",
)

############ Code to run on startup goes here

for i in range(8):
    cuinter.DialogBox.new(
        random.randrange(0, cuinter.screen_height),
        random.randrange(0, cuinter.screen_width),
        random.randrange(10, 50),
        random.randrange(10, 50),
        dialog,
    )

cuinter.ChoiceBox.new(
    cuinter.screen_height - 12,
    cuinter.screen_width // 4,
    10,
    cuinter.screen_width // 2,
    options,
)

############

while 1:
    ############ Frame calculations
    
    current_time = time.time()
    delta_time = current_time - last_time # Time since last frame
    last_time = current_time
    
    frame_count += 1
    if current_time - fps_timer >= FPS_COUNTER_REFRESH:
        average_fps = frame_count / (current_time - fps_timer)
        fps_label.config(text=f"FPS : {round(average_fps)}")
        fps_timer = current_time
        frame_count = 0
    
    ############ Cuinter event handling, code to run every frame
    
    events = cuinter.process()
    
    for event_type, value in events.items():
        match event_type:
            case "key":
                if value in (cuinter.curses.KEY_UP, ord("w")):
                    pass
                
                elif value in (cuinter.curses.KEY_DOWN, ord("s")):
                    pass
                
                elif value in (cuinter.curses.KEY_LEFT, ord("a")):
                    pass
                
                elif value in (cuinter.curses.KEY_RIGHT, ord("d")):
                    pass
                    
                elif value == ord("q"):
                    break
