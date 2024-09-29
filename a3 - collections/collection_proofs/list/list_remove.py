if __name__ == "__main__":
    l = [1, 5, 7 ,45 , 69, 10, 9, 9, 9, 12, 45]
    print(l)
    print()

    l.remove(1)
    print(l)
    print()

    del l[2]
    print(l)
    print()
    l = [e for e in l if e != 9]
    print(l)
    print()

    e = l.pop(4)
    print(e)
    print(l)
    print()

    l = list(filter(lambda item: item != 45, l))
    print(l)
    print()

    l.clear()
    print(l)