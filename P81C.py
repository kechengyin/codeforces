n = int(raw_input())
a, b = map(int, raw_input().split())
if a == b:
    print '1 ' * a + '2 ' * b
else:
    t = [[] for i in xrange(6)]
    for i, j in enumerate(map(int,raw_input().split())):
        t[j].append(i)
    if b < a:
        t = t[1] + t[2] + t[3] + t[4] + t[5]
        t.reverse()
        ret = ['1'] * n
        for i in t[:b]:
            ret[i] = '2'
        print ' '.join(ret)
    else:
        t = t[5] + t[4] + t[3] + t[2] + t[1]
        ret = ['2'] * n
        for i in t[:a]:
            ret[i] = '1'
        print ' '.join(ret)
