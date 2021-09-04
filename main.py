import time

x = input()
x = int(x)
count = 0

while x!=1:
    if x%2==1:
        x=x*3+1
    else:
        x=x/2
    count += 1
    r = str(count).zfill(4)
    print("[Step : ",r,"][x :",'{:.0f}'.format(x).rjust(10),"]")
    time.sleep(0.05)
    