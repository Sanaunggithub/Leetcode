def recoverOrder(order, friends):
    res = []

    for o in order:
        if o in friends:
            res.append(o)
