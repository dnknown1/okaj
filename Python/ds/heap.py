class Heap():
    @staticmethod
    def heapify(array, heap_size, i):
        l = 2*i+1
        r = 2*i+2 
        t = int()
        if l < heap_size and array[l] > array[i]:
            t = l
        else:
            t = i
        if r < heap_size and array[r] > array[t]:
            t = r
        if not t == i:
            array[t], array[i] = array[i], array[t]
            Heap.heapify(array, heap_size, t)
    
    @staticmethod
    def build(array):
        for i in reversed(range(len(array)//2)):
            Heap.heapify(array, len(array), i)
    
    @staticmethod
    def sort(array, heapsize=None):
        if  heapsize == None :
            heapsize = len(array) 
        for i in reversed(range(1, len(array))):
            array[0], array[i] = array[i], array[0]
            heapsize -= 1
            Heap.heapify(array, heapsize, 0)    

# test 
if __name__ == '__main__':
    import random
    from sys import argv
    n = int(argv[1]) if len(argv) > 1 else random .randint(0,16)
    while not input() == 'x':
        ar = [random.randint(0,n) for _ in range(n)]
        print('initial Array:', ar)
        print()
        Heap.build(ar)
        print('heapified array', ar)
        print()
        Heap.sort(ar)
        print('post sort:', ar)
