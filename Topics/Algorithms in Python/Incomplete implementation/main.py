def startswith_capital_counter(names):
    count = 0
    for i in range(len(names)):
        name = names[i]
        if name[0] == name[0].upper():
            count += 1
    return count
