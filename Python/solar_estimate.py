from functools import reduce

appliences = [
    {'typ': 'fan', 'qty': '4', 'pwr' :'80'},
    {'typ': 'tubelight', 'qty': '4', 'pwr' :'40'},
    {'typ': 'tv', 'qty': '2', 'pwr' :'80'},
    {'typ': 'led', 'qty': '4', 'pwr' :'9'},
    {'typ': 'bulb', 'qty': '2', 'pwr' :'60'},
    {'typ': 'pump', 'qty': '1', 'pwr' :'380'},
    {'typ': 'fridge', 'qty': '1', 'pwr' :'300'}
]
# total house load:
def pwr_lod(appliences):
    return sum(map(lambda x: int(x['pwr'])*int(x['qty']), appliences))

def cur_lod(src_vlt, pwr_lod):
    return round(pwr_lod/src_vlt, 2)

def pwr_req(src_vlt, cur_req):
    return src_vlt*cur_req

def bat_cap(pwr_lod, bck_hr, src_vlt):
    return round(pwr_lod*bck_hr/ src_vlt)

src_pwr = 350
src_vlt = 12
bck_hr = 10

p = pwr_lod(appliences)
b_c = bat_cap(p, bck_hr, src_vlt)
b_ch_cur = round(b_c/10) 
c = cur_lod(src_vlt, p)+b_ch_cur
p_r = pwr_req(src_vlt, c)
n_src = round(p_r/src_pwr)
print(
    'max_pwr', p/1000, 'kW',
    '\nbattery Capacity:', b_c, 'Ah'
    '\ncharge_current:', b_ch_cur, 'A',
    '\ncur_lod', c, 'A',
    '\nnnpwr_req', round(p_r/1000, 3), 'kW',
    f'\n{n_src+1} plates of {src_pwr} kW ie {(n_src+1)*src_pwr/1000} kW system required'
)
       