import sys
T = int(input())
for k in range(T):
    inp = input().split()
    need = int(inp[0])
    inp = inp[1]
    score = 0
    dam = 1
    for i in inp:
        if i == 'C':
            dam = dam*2
        else:
            score += dam
    need = score - need
    
    res = 0
    last = 0
    for index, i in enumerate(inp[::-1]):
        if (need <= 0):
            break
        if i == 'C':
            
            dam = dam//2
            need_move = need//dam 
            if (need%dam!=0):
                need_move += 1
            have = index - last 
            res += min(have, need_move)
            
            need = need - min(have, need_move)*dam
            last += 1
            
    if need <= 0:
        print ("Case #" + str(k+1) + ": " + str(res))
    else:
        print ("Case #" + str(k+1) + ": " + 'IMPOSSIBLE')