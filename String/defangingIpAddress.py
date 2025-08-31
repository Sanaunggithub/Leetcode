def defangIPaddr(address):
    lst = []
    for a in address:
        if a == ".":
            lst.append("[.]")

        else:
            lst.append(a)

    return "".join(lst)


address = "255.100.50.0"
print(defangIPaddr(address))