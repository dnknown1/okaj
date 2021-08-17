import numpy as np
n=11
k=2
def check(arr, low, k):
       if low+k > len(arr): return False
       return check(arr, low+1, k) if 0 in arr[low:low+k] else low+k
def sim(n,k,mc):
    mcr= np.random.randint(0, 2, (mc, n)) 
    rmap = map(lambda i: check(i,0,k), mcr)
    return sum(map(bool, rmap))/mc, mcr  

for j in range(2,21):
    print('n=', j)
    for i in [10,100,1000,10000, 100000]:
        prb, obs = sim(j, k, i)
        print(f'rpt: {i} xp({j}):  {prb}')
