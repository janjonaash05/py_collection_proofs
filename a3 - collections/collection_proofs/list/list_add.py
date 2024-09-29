if __name__ == "__main__":
    l = [1, 2]
    l += [45, 65]
    l.append(15)
    l.insert(0, 8)
    l.extend(["a", "a"])
    index = 2
    l[index:index] = [88]

    print(l)