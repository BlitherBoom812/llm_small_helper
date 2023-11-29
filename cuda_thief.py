import subprocess
import time

import psutil
def proc_exist(pid):
    pl = psutil.pids()
    return pid in pl

def cuda_thief(file_name):
    process_id = None
    while True:
        print("check existing:")
        if process_id == None or not proc_exist(process_id) or psutil.Process(process_id).status() == psutil.STATUS_ZOMBIE:
            # 如果play.py进程不存在，启动它
            print(f"start {file_name}")
            with open('output.txt', 'a') as f:
                p = subprocess.Popen(['python', file_name], stdout=f, stderr=f)
                process_id = p.pid
                print(f"pid: {process_id}")
        else:
            print(f"process status: {psutil.Process(process_id).status()}")
        # 每隔30分钟检查一次
        time.sleep(100)

if __name__ == "__main__":
    cuda_thief('play.py')
    # cuda_thief('test.py')