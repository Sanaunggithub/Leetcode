def isIsomorphic (s, t):
    if len(s) != len(t):
        return False
    
    sTot = {}
    tTos = {}

    for ss, tt in zip(s, t):
        if ss in sTot and sTot[ss] != tt:
            return False

        if tt in tTos and tTos[tt] != ss:
            return False
        
        sTot[ss] = tt
        tTos[tt] = ss
    
    return True

s = "egg"
t = "add"

print(isIsomorphic(s, t))

