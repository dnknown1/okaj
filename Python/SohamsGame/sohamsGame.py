Color: int
Container: list
Game: list

def exchange(c1, c2): c1[-1], c2[-1] = c2[-1], c1[-1]

def find(key, game):
    out = list()
    
    for loc, container in game:
        if not container[-1] and container[-2] == key: out.append(loc)
        elif all(map(lambda color: color == container[0], container[1:])): out.append(loc)

    return list(out)

def solved(game):
    reduced_game = map(lambda container: all(map(lambda color: color == container[0], container[1:])), game)
    return all(reduced_game)


game = [[1, 2], [2, 1],[0, 0]]
i = int()
while True:
    input('again')
    if solved(game): print(True); break
    loc = i%len(game)
    container = game[loc]
    if container[-1]:
        moves = find(container[-1], game)
        print(container[-1], moves); break

