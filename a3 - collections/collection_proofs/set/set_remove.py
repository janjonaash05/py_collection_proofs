if __name__ == "__main__":
    s = {1, 6, 5, 4, 9}
    s.pop()
    print(s)
    s.remove(5)  # throws if element isn't contained
    print(s)
    s.discard(5)  # doesn't throw if element isn't contained
    s.discard(6)
    print(s)
    s.clear()
    print(s)