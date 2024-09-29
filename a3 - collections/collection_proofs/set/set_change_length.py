if __name__ == "__main__":
    s = {5, 4}
    id_before = id(s)

    s.add(3)
    id_after = id(s)

    print(id_before == id_after)