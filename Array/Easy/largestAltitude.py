def largestAltitude(gain):
    s = []
    s.append(0)

    r = 0

    for g in gain:
        r += g
        s.append(r)

    print(max(s))

gain = [-4,-3,-2,-1,4,3,2]
largestAltitude(gain)