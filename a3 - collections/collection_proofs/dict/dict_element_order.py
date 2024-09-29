if __name__ == "__main__":
    # "Keeps element order T/F"
    d = {}
    d_keys = [1, 2, object, "ahoj", False, 6.5]
    for i in d_keys:
        d.update({i: object})

    keeps_order = True
    index = 0
    for e in d.keys():
        if e != d_keys[index]:
            keeps_order = False
            break
        index += 1

    print(keeps_order)
    # depends on Python version
