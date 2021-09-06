import time
from multiprocessing import Process

def calc(firstnum):
    calcnum = int(firstnum)
    count = 0

    while calcnum!=1:
        if calcnum%2==1:
            calcnum=calcnum*3+1
        else:
            calcnum=calcnum/2
        count += 1
        step = str(count).zfill(4)
        print("[Step : ",step,"][calcnum :",'{:.0f}'.format(calcnum).rjust(10),"]")
        #time.sleep(0.05)
    

if __name__ == "__main__":
    counttime = time.perf_counter()
    for i in range(1,100):
        print(i)
        calc(i)
    print(time.perf_counter() - counttime)
    print("not multiprocess done")
    input()