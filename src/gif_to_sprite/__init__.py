from .split_gif import split
from .sprite_from_images import make_spritesheet
import argparse
import os
import glob
import re

def gif_to_sprite (gif=None, mastername=None, cleanup=True):
    split(gif)
    make_spritesheet(mastername)

    if cleanup is True:
        print ('cleaning up...')
        leftovers = [ f for f in glob.glob('*.gif') if re.match(r'\d+.gif', f) ]
        for f in leftovers:
            print ('\tremove %s' % f)
            os.remove(f)
