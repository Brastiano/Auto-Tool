import pyautogui
import pygetwindow
import keyboard
import time
import threading

# TOOL CONTROL KEYS BINDING
START_KEY = '`'
STOP_KEY = '`'

# SKILL KEYS BINDING
SKILL_1_KEY = '1'
SKILL_2_KEY = '2'
SKILL_3_KEY = '3'
SKILL_4_KEY = '4'
SKILL_5_KEY = '5'
SKILL_6_KEY = '6'
SKILL_7_KEY = '7'
SKILL_8_KEY = '8'

# ALTERNATIVE KEY
ALT_KEY = 'alt'

# QUICK SLOTS
FIRST_KEY = 'q'
SECOND_KEY = 'e'

# UTILITY KEYS BINDING
COMMUNITY_KEY = 'c'
MISSION_KEY = 'j'
MAP_KEY = 'm'
TERMINAL_KEY = 't'
CHARACTER_KEY = 'p'
INVENTORY_KEY = 'i'
STORE_KEY = 'k'
SETTING_KEY = 'o'

# SKILL DURATIONS
BLIZZARD_DURATION = 10
STORM_DURATION = 5
CHARGE_DURATION = 4
FAMILIA_DURATION = 2

class AutoFarmingToram:

    RECHARGE_AFTER = 12

    TERMINATE = False

    def __init__(self, type='blizzard'):
        if type == 'blizzard':
            self.setup_keys(blizzard=SKILL_1_KEY)
        elif type == 'storm':
            self.setup_keys(storm=SKILL_1_KEY)
        else:
            self.setup_keys(blizzard=SKILL_1_KEY, storm=SKILL_2_KEY, charge=SKILL_3_KEY,
                            maximizer=SKILL_4_KEY, familia=SKILL_5_KEY)

    def setup_keys(self, blizzard=None, storm=None, charge=SKILL_2_KEY, maximizer=SKILL_3_KEY, familia=SKILL_4_KEY):
        self.BLIZZARD_KEY = blizzard
        self.STORM_KEY = storm
        self.CHARGE_KEY = charge
        self.MAXIMIZER_KEY = maximizer
        self.FAMILIA_KEY = familia

    def run(self):

        self.focus_window('ToramOnline')

        terminate_thread = threading.Thread(target=self.terminate, args=STOP_KEY)
        terminate_thread.start()

        while not self.TERMINATE:
            pyautogui.press(self.FAMILIA_KEY)
            self.sleep(FAMILIA_DURATION)
            for attempt in range(self.RECHARGE_AFTER):
                self.rotate((500, 540), (1100, 540), 0.5)
                pyautogui.press(self.BLIZZARD_KEY)
                pyautogui.press(self.BLIZZARD_KEY)
                self.sleep(BLIZZARD_DURATION)

        terminate_thread.join()

    def focus_window(self, title):
        window = pygetwindow.getWindowsWithTitle(title)[0]
        if window:
            window.activate()
        else:
            print("Window not found.")

    def rotate(self, start, end, duration):
        pyautogui.moveTo(start)
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(end, duration=duration)
        pyautogui.mouseUp(button='right')
        time.sleep(0.5)

    def terminate(self, key):
        print(f'Press {key} to terminate.')
        keyboard.wait(key)
        self.TERMINATE = True

    def sleep(self, seconds):
        # for s in range(seconds):
        #     if self.TERMINATE:
        #         break
        #     time.sleep(s)
        time.sleep(seconds)
