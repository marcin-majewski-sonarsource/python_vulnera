import os

def send_signal(pid, sig, pgid):
    #os.kill(pid, sig)  # Sensitive
    os.killpg(pgid, sig)  # Sensitive

