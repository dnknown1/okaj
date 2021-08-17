from functools import reduce

prb = [
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0]
]

def make_flat(arr): return list(reduce(lambda x, y: [*x, *y], arr))

def dflat(arr, loc):
    r, c = loc
    return list(map(lambda x: [*arr[c*x: c*(x +1)]], range(r)))

def floc(loc, c): return c*loc[0] + loc[1]
def dfloc(floc, c): return floc//c, floc%c

####
r, c = len(prb), len(prb[0])
fprb = make_flat(prb)
dfprb = dflat(fprb, (r, c))
fidx = floc((3, 4), c) 
dfidx = dfloc(fidx, c)

####################
print(prb[3][4], fprb[fidx], dfprb[dfidx[0]] [dfidx[1]])
fprb[fidx] = 5
print(prb[3][4], fprb[fidx])