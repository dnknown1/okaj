import concurrent.futures as res
import time
from math import log, ceil

def ms_delay(delay):
    #print(f'initiating {delay} ms delay')
    time.sleep(delay/1000)
    #print(f'{delay} ms delay executed')
    sum(range(1,1_000_001))


"""def test(fun):
    def evaluate(*args):
        ts = time.perf_counter()
        fun(*args)
        tf = time.perf_counter()
        print(f'{args[0]} tasks: {args[1]}ms in {round(tf-ts, 3)}s')
    return evaluate

@test
def sequential(n_task, delay):
    for _ in range(n_task):
        ms_delay(delay)        

#
# TEST BENCH 
#delay_time = 10
#for task in (10, ):
#    print('sequential')
#    sequential(task, delay_time)
#    print('parallel')
#    parallel(task, delay_time)

#@test
def parallel (n_task, delay):
    with res.ThreadPoolExecutor(max_workers= n_task) as executor:
        results = executor.map(ms_delay, (delay for _ in range(n_task)))
##"""########################
def add_em(a, b, delay=.3): 
    time.sleep(delay/1000)
    #print(a,b, 'in add_em')
    return a+b

def dummy(size): return list(range(1, size+1))

def test(fun):
    def evaluate(*args):
        ts = time.perf_counter()
        ans = fun(*args)
        tf = time.perf_counter()
        return ans, round(tf-ts, 3)
    return evaluate

@test
def seq_sum(mem):
    result = mem[0]
    for i in  mem[1:]:
        result = add_em(result, i)
    return result 


def broadcast(r):
    return [(r[i], r[i+1] if i < len(r)-1 else 0) for i in range(0, len(r), 2)]

@test
def par_sum(mems):
    b = broadcast(mems)
    n = len(b)
    while b[0][1]:
        with res.ThreadPoolExecutor(max_workers= n) as executor:
             r = executor.map(lambda x: add_em(*x), b)
             b = broadcast([*r])
             n = len(b)
    return b[0][0]

mems = [2, 3, 4, 5, 10, 25, 50, 100, 250, 500, 1000, 10000, 25000]
for v in map(dummy, mems):
    for l, algo in enumerate([seq_sum, par_sum]):
        r, t = algo(v)
        print('p' if l else'S',
                '-> items:', len(v),
                '-> result:', r,
                '-> time:', t, 'ms')
    print('\n')