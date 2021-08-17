# Based on cheer Park 
# creates snap: zip object zip(x, [dict() for d in range( len(x))])
def add_snap(tbl, g, c, s, obs): 
   snap = ( 'fps' ,'cpu', 'gpu')
   t = tbl.copy()
   t[g][c][s]['snaps'].append(dict(zip(snap, obs)))
   return t 

# initiate lookup table
def init_table() :
    return {
    'smt': {
        'utr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        },
        'xtr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        } 
    },
    'bal': {
        'utr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        },
        'xtr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        } 
    },
    'hd': {
        'utr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        },
        'xtr': {
            "cls": { 'snaps': []},
            "clr" : { 'snaps': []},
            "rel" : { 'snaps': []},
            'mvi' : { 'snaps': []}
        } 
    }
}

def predict(t, g, c, s):
    sms = [0, 0, 0, 0]
    for i in t[g][c][s]['snaps']:
         sms[0] += i['fps']
         sms[1] += i['cpu']
         sms[2] += i['gpu']
         sms[3] += 1
    return tuple(map(lambda x: x//sms[-1], sms[:-1]))


# Driver
render_styles = ("cls",  "clr",  "rel",  'mvi')
graphics = ('smt')
cpu_load = ( 'xtr')

def read_data(t, g, c, s, n):
    for i in g:
        for j in c:
            for k in s:
                for _ in range(n): t = add_snap(t , i, j, k, map(int, input(f'type in for {i} - {j} - {k} of obs {_+1}:\t').split()))
 


#read_data(tbl, graphics, cpu_load, render_styles, 15)
#tbl = add_snap(tbl, 'smt', 'xtr', 'cls', (52,76,96))
#tbl = add_snap(tbl, 'smt', 'xtr', 'cls', (55,70,99))
cl  = [
    (48, 43, 99),
    (42, 41, 99),
    (38, 52, 71),
    (38, 37, 90),
    (32, 29, 99),
    (33, 33, 96),
    (38, 50, 77),
    (31, 32, 99),
    (32, 25, 79),
    (30, 30, 99),
    (41, 41, 99),
    (49, 33, 82),
    (41, 34, 81),
    (46, 37, 73),
    (42, 37, 99)
]
cr = [
    (29, 32, 99),
    (39, 33, 83),
    (35, 28, 99),
    (41, 40, 77),
    (38, 34, 98),
    (54, 34, 99),
    (53, 31, 95),
    (53, 27, 95),
    (56, 33, 99),
    (55, 25, 98),
    (40, 28, 99),
    (39, 41, 94),
    (43, 42, 95),
    (38, 36, 82),
    (38, 37, 81)
]
rel = [
    (42, 36, 99),
    (45, 41, 99),
    (48, 40, 98),
    (43, 23, 77),
    (51, 27, 99),
    (57, 35, 88),
    (58, 26, 92),
    (57, 32, 84),
    (58, 31, 96),
    (59, 29, 75),
    (37, 40, 99),
    (48, 35, 94),
    (38, 26, 79),
    (45, 35, 88),
    (32, 37, 54)
]
mvi = [
    (39, 34, 99),
    (44, 36, 80),
    (28, 52, 67),
    (32, 34, 99),
    (36, 32, 92),
    (37, 37, 99),
    (32, 34, 47),
    (38, 42, 99),
    (48, 37, 98),
    (41, 48, 99),
    (38, 40, 99),
    (40, 37, 96),
    (41, 36, 99),
    (36, 33, 98),
    (38, 32, 98)
]

tbl = init_table()
for i in cl: tbl = add_snap(tbl,  'smt',  'xtr',  'cls', i)
for i in cr: tbl = add_snap(tbl,  'smt',  'xtr',  'clr', i)
for i in rel: tbl = add_snap(tbl,  'smt',  'xtr',  'rel', i)
for i in mvi: tbl = add_snap(tbl,  'smt',  'xtr',  'mvi', i)    
#print(tbl)
for i in render_styles:
    print(f"Avg Performance for {i}:", predict(tbl, 'smt', 'xtr',: i))