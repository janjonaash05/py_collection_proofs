if __name__ == "__main__":
    # "Keeps element order T/F"
    st = ""
    st_list = ['a', 'w', '0', 'g', 'A']
    for i in st_list:
        st += i

    keeps_order = True
    index = 0
    for e in st:
        if e != st_list[index]:
            keeps_order = False
            break
        index += 1

    print(keeps_order)
