n, k = map(int, raw_input().split())
s = raw_input()
print "NO" if s.find('#'*k) != -1 else "YES"