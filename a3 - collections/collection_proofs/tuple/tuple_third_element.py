if __name__ == "__main__":
    t = (1, 8, -5)

    print(t[2])

    index = 0
    for e in t:
        if index == 2:
            print(e)
            break
        index += 1
