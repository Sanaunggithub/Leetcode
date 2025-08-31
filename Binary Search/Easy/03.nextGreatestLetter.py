def nextGreatestLetter(letters, target):
    max = letters[0]
    
    for i in range(len(letters)):
        if target == letters[i]:
            continue
        
        elif letters[i] > target:
            return letters[i]

    return max

letters = ["x","x","y","y"]
target = "z"

print(nextGreatestLetter(letters, target))