if __name__ == "__main__":
    st = "abc"
    id_before = id(st)

    st += "de"
    id_after = id(st)

    print(id_before == id_after)