#! /usr/bin/python

# split-gif
# Jordan Timmerman

import tempfile
import sys
from PIL import Image

def split (gif):
    gif = gif[0]

    print('%s will be split...' % gif)

    frame = Image.open(gif)
    frameIdx = 0

    try:
        while 1:
            print('\tseek frame %d' % frameIdx)
            frame.seek( frameIdx )
            print('\tsave frame %d' % frameIdx)
            frame.save( '%s/%s.gif' % (tempfile.gettempdir(), frameIdx), 'GIF' )
            frameIdx += 1
    except EOFError:
        print('done.')
        pass

    return frameIdx

if __name__ == '__main__':
    split(sys.argv[1])
