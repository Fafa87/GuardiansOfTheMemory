from __future__ import print_function

import time

import xandor

if not xandor.is_root() and not xandor.has_debugger():
    xandor.elevate_me()
    exit(0)


def draox_sentry(angry):
    mem, sw = xandor.get_current_memory()
    # do not kill if angry (so only one is killed)
    if mem["taken"] > 95 and not angry:
        big = xandor.find_proc_with_most_memory()
        print("There is too much memory taken... ", mem["taken"])
        print(big.name(), "is misbehaving... die! die! die!")
        big.kill()
        return True

    return mem["taken"] > 95


print("Draox starts to defend...")

angry = False
while True:
    angry = draox_sentry(angry)
    time.sleep(0.5)
