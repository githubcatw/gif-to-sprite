# gif to sprite python library

![Derp Horse](https://raw.githubusercontent.com/skorlir/gif-to-sprite/6f9690591316dfd1142f4bbc4c4deda5f013d856/example/derp-horse.gif)

The original script has been converted into a library.

### Usage

`python -m src\gif_to_sprite example/derp-horse.gif example/master.jpg`

### Basics

There's one command line flag for 'messy' - ie, don't delete intermediary
frames that are extracted from the gif.

`python -m src\gif_to_sprite -m example/derp-horse.gif example/master.jpg`

This will result in {0, 1, 2, ...}.gif being placed in current working dir.
These files correspond to frames extracted from the gif, in order.

### Todo

Generate CSS sprite stylesheet for example testing
