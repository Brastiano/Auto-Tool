# Libraries
import time

# Scripts
from src.toram import AutoFarmingToram

if __name__ == '__main__':

    print('Script starts running...`')
    start = time.time()

    auto = AutoFarmingToram()
    auto.run()

    end = time.time()
    print('Script stops running...')

    print('Time elapsed:', round(end - start, 2))

