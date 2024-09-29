if __name__ == "__main__":

    result = ""
    try:
        nested = f"{(12, 3)}"
        result += "Tuples allowed,"
    except TypeError:
        result += "Tuples not allowed,"
    try:
        nested = f"{[12, 3]}"
        result += "Lists allowed,"
    except TypeError:
        result += "Lists not allowed,"
    try:
        nested = f"{ {12, 3} }"
        result += "Sets allowed,"
    except TypeError:
        result += "Sets not allowed,"
    try:
        nested = f"{ {12: 3} }"
        result += "Dicts allowed,"
    except TypeError:
        result += "Dicts not allowed,"
    try:
        nested = f"{ str('a') }"
        result += "Strings allowed,"
    except TypeError:
        result += "Strings not allowed,"
    print(result)
