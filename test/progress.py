from rich.progress import track
import time

for step in track(range(1)):
    #do_step(step)
    if step == 50:
        exit(1)
    time.sleep(10)

