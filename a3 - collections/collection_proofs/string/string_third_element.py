if __name__ == "__main__":
    st = "abc"

    print(st[2])

    index = 0
    for e in st:
        if index == 2:
            print(e)
            break
        index += 1