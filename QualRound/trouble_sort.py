import sys
T = int(input())
for k in range(T):
    N = int(input())
    res = 'OK'
    inp = list(map(int, input().split()))
    l1 = []
    l2 = []
    for i in range(0,N,2):
        l1.append(inp[i])
        if i < N-1:
            l2.append(inp[i+1])
    l1 = sorted(l1)
    l2 = sorted(l2)
    l1.append(1000000001)
    for i in range(len(l2)):
        if (l2[i] >= l1[i] and l2[i] <= l1[i+1]):
            continue
        if (l2[i] < l1[i]):
            res = i*2
            break
        if (l2[i] > l1[i+1]):
            res = i*2+1
            break
        
    print ("Case #" + str(k+1) + ": " + str(res))