import os
import datetime as dt
def main():
    return os.system("shutdown /s /t 1")

time=dt.datetime.today()
our_time=time.hour
off_time=21
if our_time==off_time:
    main()
else:
    exit()