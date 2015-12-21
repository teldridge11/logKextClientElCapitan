import subprocess
import time
import daemon

def logKextClientKillLoop():
    '''Kill the keylogger daemon.'''
    while True:
        subprocess.call(['pkill', 'logKextDaemon'])
        time.sleep(3600)

def run():
    with daemon.DaemonContext():
        logKextClientKillLoop()

if __name__ == "__main__":
    run()
