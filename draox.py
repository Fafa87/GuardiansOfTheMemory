from __future__ import print_function

import time

import xandor

if not xandor.is_root():
    xandor.elevate_me()
    exit(0)


def draox_sentry():
    mem, sw = xandor.get_current_memory()
    if mem["taken"] > 95:
        big = xandor.find_proc_with_most_memory()
        print("There is too much memory taken... ", mem["taken"])
        print(big.name(), "is misbehaving... die! die! die!")
        big.kill()


print("Draox starts to defend...")

while (True):
    draox_sentry()
    time.sleep(0.5)
