if __name__ == "__main__":
    # Sorted lower->upper when element added T/F

    d = {5: "ahoj", 7: True, 6: object}
    d2 = {5: "ahoj", 7: True, 6: object}
    print(d.keys() == sorted(d.keys()))
    print(d == d2)
