if __name__ == "__main__":
    s = {1, 2}
    s.add(15)
    s = s.union({"a", 14})

    print(s)