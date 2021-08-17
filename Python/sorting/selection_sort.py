def selection_sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] or a[j] > a[i]:
                a[i],a[j] = a[j], a[i]
                #print(a)
    return a

print(selection_sort([5,6,5,3,2,6,7,8,9,5,2,0,1]))