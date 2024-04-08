# Libraries
import time

# Scripts
from src import toram
from src import simplemmo

if __name__ == '__main__':

    print('Script starts running...`')
    start = time.time()

    # auto = toram.AutoFarmingToram()
    auto = simplemmo.AutoProgress('light-mode')
    # auto = simplemmo.AutoProgress('dark-mode')
    auto.run()

    end = time.time()
    print('Script stops running...')

    print('Time elapsed:', round(end - start, 2))

