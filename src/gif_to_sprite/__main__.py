import argparse

from . import gif_to_sprite

parser = argparse.ArgumentParser(
    description='Make a spritesheet from an animated gif.'
)
parser.add_argument('gif', metavar='gif', type=str, nargs=1)
parser.add_argument('mastername',
                    help='Output spritesheet name (w/ extension)',
                    metavar='', type=str, nargs='?', default=None)
parser.add_argument('-m', '--no-cleanup', dest='cleanup',
                    help='leave a mess / don\'t clean up frames',
                    action='store_false')

args = parser.parse_args()

gif_to_sprite(gif=args.gif, mastername=args.mastername, cleanup=args.cleanup)
