class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def insert_node(root, data):
    if data >= root.data:
        if not root.right:
            print(f'\t * Inserting {data} at right of {root.data} ')
            root.right = Node(data)
        else:
            insert_node(root.right, data)
    else:
        if not root.left:
            print(f'\t * Inserting {data} at left of {root.data} ')
            root.left = Node(data)
        else:
            insert_node(root.left, data)


if __name__ == '__main__':
    import random
    n = 7
    while not input() == 'x':
        root = Node(random.randint(0, n))
        print('Tree Generated With Root :', root.data)
        
        for i in range(n):
            x = random.randint(0, n)
            print("\tInserting :", x)
            insert_node(root, x)
            
        print('Generation Complete')
        print('Viewing All left children of:', root.data)
        x = root
        while x.left:
            print('\t', x.left.data)
            x = x.left
        print('Viewing All right children of:', root.data)
        x = root
        while x.right:
            print('\t', x.right.data)
            x = x.right
