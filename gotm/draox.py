from __future__ import print_function

import time

import gotm.xandor

THRESHOLD = 93


def roar():
    print('\a')
    time.sleep(0.5)
    print('\a')
    time.sleep(1)


def draox_sentry(angry):
    mem, sw = gotm.xandor.get_current_memory()
    # do not kill if angry (so only one is killed)
    if mem["taken"] > THRESHOLD and not angry:
        big = gotm.xandor.find_proc_with_most_memory()
        print("There is too much memory taken... ", mem["taken"])
        print(big.name(), "is misbehaving... die! die! die!")
        big.kill()
        roar()
        print("calming down...")
        time.sleep(2)
        print("... ready to go")
        return True

    return mem["taken"] > THRESHOLD


if __name__ == "__main__":
    if not gotm.xandor.is_root() and not gotm.xandor.has_debugger():
        gotm.xandor.elevate_me()
        exit(0)

    print("Draox starts to defend...")

    angry = False
    while True:
        angry = draox_sentry(angry)
        time.sleep(0.5)
