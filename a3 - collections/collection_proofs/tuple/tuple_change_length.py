if __name__ == "__main__":
    t = (5, 4)
    id_before = id(t)

    t += (4, 6)
    id_after = id(t)

    print(id_before == id_after)