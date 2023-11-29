import psutil
def proc_exist(pid):
    pl = psutil.pids()
    return pid in pl


if __name__ == "__main__":
    print(proc_exist(901758))