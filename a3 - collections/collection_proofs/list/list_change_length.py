if __name__ == "__main__":
    l = [5, 4]
    id_before = id(l)

    l.append(3)
    id_after = id(l)

    print(id_before == id_after)