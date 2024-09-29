if __name__ == "__main__":
    # Can insert identical elements
    s = {1, 2, 3, 4}
    s_same = {1, 2, 3, 3}
    print(len(s) == len(s_same))
