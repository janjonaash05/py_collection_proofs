if __name__ == "__main__":
    l = [1, 8, -5]

    print(l[2])

    index = 0
    for e in l:
        if index == 2:
            print(e)
            break
        index += 1