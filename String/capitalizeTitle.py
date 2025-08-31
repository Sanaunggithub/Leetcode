def capitalizeTitle(title):
    lst = title.split()
    rst = []
    for word in lst:
            if len(word) < 3:
                rst.append(word.lower())
            
            else:
                rst.append(word.title())
    return " ".join(rst)

print(capitalizeTitle("First leTTeR of EACH Word"))