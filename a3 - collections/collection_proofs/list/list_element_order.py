if __name__ == "__main__":
    # "Keeps element order T/F"
    l = [1, 2, object, "ahoj", False, 6.5]
    l_copy = []
    for i in l:
        l_copy.append(i)

    keeps_order = True
    index = 0
    for e in l:
        if e != l_copy[index]:
            same_elements = False
            break
        index += 1

    print(keeps_order)