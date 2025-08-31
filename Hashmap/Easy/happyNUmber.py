def isHappy(n):
    seen = set()
    
    while True:
        if n in seen: # start the cycle
            return False
        
        if n == 1:
            return True
        
        seen.add(n) # keep full number in set to compare

        lst = []
        for c in str(n):
            lst.append(int(c)**2)
        

        n = sum(lst)
        
 
    

n = 19
print(isHappy(n))