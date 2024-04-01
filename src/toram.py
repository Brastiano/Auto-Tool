import pyautogui
import pygetwindow
import keyboard
import time
import threading

class AutoFarmingToram:

    BLIZZARD_DURATION = 10
    SPAWN_FAMILIAR_DURATION = 3
    RECHARGE_AFTER = 12
    STOP = False
    TERMINATE_KEY = '`'

    BLIZZARD_KEY = '1'
    SPAWN_FAMILIAR_KEY = '7'

    def run(self):

        print('Script starts running...')
        start = time.time()

        self.focus_window('ToramOnline')

        terminate_thread = threading.Thread(target=self.terminate, args=self.TERMINATE_KEY)
        terminate_thread.start()

        while not self.STOP:
            pyautogui.press(self.SPAWN_FAMILIAR_KEY)
            self.sleep(self.SPAWN_FAMILIAR_DURATION)
            for attempt in range(self.RECHARGE_AFTER):
                pyautogui.press(self.BLIZZARD_KEY)
                pyautogui.press(self.BLIZZARD_KEY)
                self.sleep(self.BLIZZARD_DURATION)

        terminate_thread.join()

        end = time.time()
        print('Script stops running...')

        print('Time elapsed:', round(end-start, 2))

    def focus_window(self, title):
        window = pygetwindow.getWindowsWithTitle(title)[0]
        if window:
            window.activate()
        else:
            print("Window not found.")

    def setup_buttons(self):
        pass

    def auto_sell(self):
        pass

    def terminate(self, key):
        print(f'Press {key} to terminate.')
        keyboard.wait(key)
        self.STOP = True

    def sleep(self, seconds):
        # for s in range(seconds):
        #     if self.STOP:
        #         break
        #     time.sleep(s)
        time.sleep(seconds)
