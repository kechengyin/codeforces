n = int(raw_input())
stairs = map(int, raw_input().split())
k = int(raw_input())
for case in xrange(k):
    w, h = map(int, raw_input().split())
    p = max(stairs[0], stairs[w-1])
    print p
    stairs[0] = p + h