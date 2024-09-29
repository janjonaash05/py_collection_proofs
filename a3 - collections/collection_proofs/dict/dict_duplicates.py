if __name__ == "__main__":
    # Can insert identical elements
    d = {1: 2, 5: 6, 7: 9}
    d_dup_keys = {1: 2, 1: 6, 7: 9}
    d_dup_values = {1: 2, 5: 2, 7: 2}
    print(len(d) == len(d_dup_keys))
    print(len(d) == len(d_dup_values))
