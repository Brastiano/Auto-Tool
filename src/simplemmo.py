import pyautogui
import pygetwindow
import keyboard
import time

# PATHS
IMAGES = 'images/simplemmo/'

# TOOL CONTROL KEYS BINDING
START_KEY = '`'
STOP_KEY = '`'


class AutoProgress:

    TERMINATE = False

    def __init__(self, mode):
        self.mode = mode

    def run(self):

        self.focus_window('Opera')

        time.sleep(1)

        while not self.TERMINATE:
            self.step()
            time.sleep(1)
            self.battle()
            time.sleep(1)
            self.gather_resources()
            time.sleep(1)


    def focus_window(self, title):
        try:
            window = pygetwindow.getWindowsWithTitle(title)[0]
            window.activate()
        except Exception:
            print('Window not found.')

    def step(self):
        try:
            button = IMAGES + self.mode + '/step-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/step-button-hover.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
        except Exception:
            pass

    def gather_resources(self):
        self.chop()
        self.mine()
        self.salvage()
        self.fish()

    def chop(self):
        to_gather = self.to_gathering_interface('chop')
        if to_gather:
            self.interact_gathering_interface()

    def mine(self):
        to_gather = self.to_gathering_interface('mine')
        if to_gather:
            self.interact_gathering_interface()

    def salvage(self):
        to_gather = self.to_gathering_interface('salvage')
        if to_gather:
            self.interact_gathering_interface()

    def fish(self):
        to_gather = self.to_gathering_interface('fish')
        if to_gather:
            self.interact_gathering_interface()

    def to_gathering_interface(self, resource):
        try:
            button = IMAGES + self.mode + '/' + resource + '-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(2)
            return True
        except Exception:
            return False

    def interact_gathering_interface(self):
        while True:
            if self.exit_gathering_interface():
                break
            else:
                self.gather()

    def gather(self):
        try:
            button = IMAGES + self.mode + '/gather-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(1)
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/gather-button-hover.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(1)
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/press-to-gather-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(1)
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/press-to-gather-button-hover.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(1)
        except Exception:
            pass

    def exit_gathering_interface(self):
        try:
            button = IMAGES + self.mode + '/not-enough-gathering-level-text.png'
            pyautogui.locateOnScreen(button, confidence=0.9)
            button = IMAGES + self.mode + '/go-back-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            return True
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/press-to-close-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            return True
        except Exception:
            pass
        try:
            button = IMAGES + self.mode + '/press-to-close-button-hover.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            return True
        except Exception:
            return False

    def battle(self):
        to_battle = self.to_battle_interface()
        if to_battle:
            self.interact_battle_interface()

    def to_battle_interface(self):
        try:
            button = IMAGES + self.mode + '/attack-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            time.sleep(2)
            return True
        except Exception:
            return False

    def interact_battle_interface(self):
        while True:
            if self.exit_battle_interface():
                break
            else:
                self.attack()

    def attack(self):
        try:
            button = IMAGES + self.mode + '/attack-button-in-battle.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
        except Exception:
            pass

    def exit_battle_interface(self):
        try:
            button = IMAGES + self.mode + '/end-battle-button.png'
            location = pyautogui.locateOnScreen(button, confidence=0.9)
            pyautogui.click(location)
            return True
        except Exception:
            return False

    def to_robot_interface(self):
        pass