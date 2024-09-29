if __name__ == "__main__":
    d = {5: 4}
    id_before = id(d)

    d.update({3: 4})
    id_after = id(d)

    print(id_before == id_after)