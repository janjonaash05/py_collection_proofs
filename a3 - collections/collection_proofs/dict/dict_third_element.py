if __name__ == "__main__":
    d = {"a": 45, "b": 78, object: "c"}
    index = 0
    for e in d:
        if index == 2:
            print(f"{e}:{d[e]}")

            break
        index += 1
