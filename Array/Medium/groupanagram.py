def groupAnagrams(strs):
    output = {} # mapping charCount to list of anagrams
    
    for s in strs:
        count = [0] * 26 # count of a ... z initially sets to 0 

        for c in s:
            count[ord(c) - ord("a")] += 1
            #  a = 80 -> 0, 80 - 80 
            #  b = 81 -> 1, 81 - 80 (b - a)

        # lists can’t be keys, but tuples can
        key = tuple(count)

        # if key exists, append to the list, or create a new list
        output[key] = output.get(key, []) + [s]

    
    return list(output.values())


strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
