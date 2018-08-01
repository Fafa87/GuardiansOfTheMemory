import os
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    assert name, name
    ls = []
    for p in psutil.process_iter():
        name_, exe, cmdline = "", "", []
        try:
            name_ = p.name()
            cmdline = p.cmdline()
            exe = p.exe()
        except (psutil.AccessDenied, psutil.ZombieProcess):
            pass
        except psutil.NoSuchProcess:
            continue
        if name == name_ or cmdline[0] == name or os.path.basename(exe) == name:
            ls.append(name)
    return ls
    
    
def find_proc_with_most_memory():
    for p in psutil.process_iter():
    
        try:
                name_ = p.name()
                cmdline = p.cmdline()
                exe = p.exe()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except psutil.NoSuchProcess:
                continue

    return max(psutil.process_iter(), key=psutil.Process.memory_percent)

    
def get_current_memory():
    virt = psutil.virtual_memory()
    res = {"all": int(virt.total >> 20),
          "taken" : virt.percent,
          "used" : int(virt.used >> 20),
          "free" : int(virt.free >> 20)}
    swap = psutil.swap_memory()
    swap = {"all": int(swap.total >> 20),
          "taken" : swap.percent,
          "used" : int(swap.used >> 20),
          "free" : int(swap.free >> 20)}
    return res, swap