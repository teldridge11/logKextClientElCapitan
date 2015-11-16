import subprocess
import time
import daemon

def loop_kill_logKextClient():
    '''Kill the keylogger daemon.'''
    while True:
        subprocess.call(['pkill', 'logKextDaemon'])
        time.sleep(3600)

def run():
    with daemon.DaemonContext():
        loop_kill_logKextClient()

if __name__ == "__main__":
    run()
