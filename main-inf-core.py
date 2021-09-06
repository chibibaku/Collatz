import time
#import os
#from multiprocessing import Process
from multiprocessing import Pool

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
        calcnum_out = str(firstnum).zfill(4)
        print("[Num : ",calcnum_out,"][Step : ",step,"][calcnum :",'{:.0f}'.format(calcnum).rjust(10),"]")
    

if __name__ == "__main__":
    counttime = time.perf_counter()
    for i in range(1,5000):
        with Pool(processes=8) as pool:
            pool.map(calc, range(i))
        #p = Process(target=calc, args=(i,10))        
        #p.start()
    
    print(time.perf_counter() - counttime)
    print("multiprocess done")
    input()
    #p.join()