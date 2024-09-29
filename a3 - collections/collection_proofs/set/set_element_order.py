if __name__ == "__main__":
    # "Keeps element order T/F"
    s = set({})
    s_list = [1, 2, object, "ahoj", False, 6.5]
    for i in s_list:
        s.add(i)

    keeps_order = True
    index = 0
    for e in s:
        if e != s_list[index]:
            keeps_order = False
            break
        index += 1

    print(keeps_order)
