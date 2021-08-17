from math import comb, factorial 
def p_alive(m, n):
    return sum(map(lambda x: comb(m, x), range(n)))/factorial(m)
print(p_alive(7,3))
