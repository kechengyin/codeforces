n, k = map(int, raw_input().split())
t = sorted(map(int,raw_input().split()))
c = 1.0 - k / 100.0
total = sum(t)
less = 0
for i in xrange(n):
    more = total - less
    p = (more * c + less) / (i + (n - i ) * c )
    less += t[i]
    if p <= t[i]:
        print p
        break
