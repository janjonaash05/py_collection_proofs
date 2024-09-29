if __name__ == "__main__":
    d = {75: object, "ah": False, 6: 8}
    print("ah" in d)
    print(object in d.values())
    print(75 in d and object == d[75])
