if __name__ == "__main__":
    result = ""
    try:
        nested = ((12, 3), 1)
        result += "Tuples allowed,"
    except TypeError:
        result += "Tuples not allowed,"
    try:
        nested = ([12, 3], 1)
        result += "Lists allowed,"
    except TypeError:
        result += "Lists not allowed,"
    try:
        nested = ({12, 3}, 1)
        result += "Sets allowed,"
    except TypeError:
        result += "Sets not allowed,"
    try:
        nested = ({12: 3}, 1)
        result += "Dicts allowed,"
    except TypeError:
        result += "Dicts not allowed,"
    try:
        nested = ("aa", 1)
        result += "Strings allowed,"
    except TypeError:
        result += "Strings not allowed,"

    print(result)