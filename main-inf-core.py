import time
#import os
#from multiprocessing import Process
from multiprocessing import Pool

def calc(firstnum):
    #calcnum = int(firstnum)
    #count = 0
    
    for loop in range(9):
        calcnum = int(firstnum+ loop)
        calcnum_out = str(calcnum).zfill(4)
        #print("====================================================")
        print("[Num : ",calcnum_out,"][Step : Start ][calcnum :",'{:.0f}'.format(calcnum).rjust(10),"]")
        #print(loop , calcnum)
        count = 0

        while calcnum!=1:
            if calcnum%2==1:
                calcnum=calcnum*3+1
            else:
                calcnum=calcnum/2
            count += 1
            step = str(count).zfill(4)
            print("[Num : ",calcnum_out,"][Step : ",step,"][calcnum :",'{:.0f}'.format(calcnum).rjust(10),"]")
            #time.sleep(1)

        
    

if __name__ == "__main__":
    deamon = True
    counttime = time.perf_counter()
    for i in range(1,5000):
        pool = Pool(1)
        pool.apply_async(calc(i))
        #p = Process(target=calc, args=(i,10))        
        #p.start()
        i += 100
    
    print(time.perf_counter() - counttime)
    print("multiprocess done")
    input()
    #p.join()