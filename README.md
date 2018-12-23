# GuardiansOfTheMemory

Guardians of the memory stand between you and very dark and grim times, where life is lost, dispair spreads like a disease and basically you have to redo all unsaved work.


## Why?

- protection against the danger when working with huge data / objects
- it is a general solution to any source of memory usage overload (e.g python, ImageJ)
- paging can allow to allocate more memory than physically available by saving
previously allocated data on disc
- however when more memory is actively used that phisically available and paging is on
everything freezes and commonly reset is necessary
- more musing on it [link]

## What?

- `draox.py` - the first protector: crude, not sophisticated but does the work

## Tests?

You can check if it stops our sample offenders, just run `draox.py` and then run one of them.

## Success stories?

- "I've loaded big tiff into ImageJ, then I wanted to load the results of its processing. It takes a while so I stopped tracking that.
After a few minutes I wanted to go back to it but could not find ImageJ anywhere. That's when I noticed Draox smile at me.
Thanks for saving me!" - Richard Bubblegum

- "I had to run code 3 times then run it with debugger to notice that it stops because Draox is continously terminating it!
Still I was saved every time!" - Bill Kickass

![image](https://user-images.githubusercontent.com/9865688/43545780-159bd1da-95d7-11e8-9dcc-4db86dbe9420.png)
