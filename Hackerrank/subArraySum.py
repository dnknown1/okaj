def share_chocolate(s, d, m):
    count = 0
    for i in range(len(s)-m):
        if sum(s[i:i+m]) ==d:
            count += 1
    return count

_ =input()
s = list(map(int, input().split()))
d, m = map(int, input().split())
print(share_chocolate(s, d, m))