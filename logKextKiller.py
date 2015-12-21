import subprocess
import time
import daemon

# Loop to kill the key logger daemon
def logKextClientKillLoop():
    while True:
        subprocess.call(['pkill', 'logKextDaemon'])
        time.sleep(3600)

# Run the kill loop with dameon context
def run():
    with daemon.DaemonContext():
        logKextClientKillLoop()

# If name is 'main' run the kill loop
if __name__ == "__main__":
    run()
