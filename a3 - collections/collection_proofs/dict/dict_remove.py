if __name__ == "__main__":
    d = {1: 45, object: 47, "a": False, 74: 15}
    print(d)
    a = d.pop(object)
    print(d)
    print(a)
    a = d.popitem()
    print(d)
    print(a)
    d.clear()
    print(d)