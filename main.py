import time

x = input()
x = int(x)

while x!=1:
    if x%2==1:
        x=x*3+1
    else:
        x=x/2
    print(x)
    time.sleep(0.05)