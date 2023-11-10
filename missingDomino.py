def getMissingTile(dominos):
    possibilities = set("%i-%i" % (i, j) for i in range(0, 6 + 1) for j in range(0, 6 + 1))
    for dom in dominos:
        if dom in possibilities:
            possibilities.remove(dom)

    if len(possibilities) == 0:
        return None
    else:
        return possibilities.pop()

print(getMissingTile(["0-0", "0-1", "1-2", "2-3"]))