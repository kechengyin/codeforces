def isRight(points):
    line1 = (points[0] - points[2]) ** 2 + (points[1] - points[3]) ** 2
    line2 = (points[0] - points[4]) ** 2 + (points[1] - points[5]) ** 2
    line3 = (points[2] - points[4]) ** 2 + (points[3] - points[5]) ** 2
    total = line1 + line2 + line3
    if 0 in (line1, line2, line3):
        return False
    if (total / 2) in (line1, line2, line3):
        return True
    else:
        return False
points = list(map(int, raw_input().split()))

if isRight(points):
    print "RIGHT"
else:
    ret = "NEITHER"
    for i in xrange(6):
        points[i] -= 1
        if isRight(points):
            ret = "ALMOST"
            break
        points[i] += 2
        if isRight(points):
            ret = "ALMOST"
            break
        points[i] -= 1
    print ret

