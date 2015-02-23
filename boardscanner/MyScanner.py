__author__ = 'Eshaan'

import pyscreenshot as ImageGrab


if __name__ == '__main__':
    currImage = ImageGrab.grab()
    print(currImage.size, currImage.format)
