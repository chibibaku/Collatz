import time


start = time.perf_counter()

def calc(x,tgt,count,):
    while x!=1:
        if x%2==1:
            x=x*3+1
        else:
            x=x/2
        count += 1
        print("[Num : ",'{:.0f}'.format(tgt).rjust(10),"]","[Step : ",str(count).zfill(4),"]","[x :",'{:.0f}'.format(x).rjust(10),"]")
        #time.sleep(0.05)
    return count

for tgt in range(1, 5000):
    log = calc(tgt,tgt,0)
    #print(log)
    tgt += 1


print(time.perf_counter() - start)
input()
