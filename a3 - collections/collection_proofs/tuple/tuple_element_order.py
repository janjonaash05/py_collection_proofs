if __name__ == "__main__":
    # "Keeps element order T/F"
    t = (1, 2, object, "ahoj", False, 6.5)
    t_list = []
    for i in t:
        t_list.append(i)

    keeps_order = True
    index = 0
    for e in t:
        if e != t_list[index]:
            same_elements = False
            break
        index += 1

    print(keeps_order)





