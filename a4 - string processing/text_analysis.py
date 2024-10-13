import re


def word_count(text):


    word_pattern = re.compile("([A-Ž][a-ž])+")
    ordered_num_pattern = re.compile("[0-9]+[a-ž]+")
    city_pattern = re.compile("[0-9]+\s[A-Ž][a-ž]+,\s([A-Ž][a-ž]*)\s(([A-Ž][a-ž]*)|[a-ž]*\s)*")
    date_pattern = re.compile("([A-Ž][a-ž]+\s([0-9]+[a-ž]{2})\s[0-9]{4})")
    short_forms = re.compile("(can't|((?<=')[a-žA-Ž]*)|([a-žA-Ž]*)')")

    return len(re.findall("(\s*[a-zA-Z]+(\s|,)*)", text))


if __name__ == '__main__':
    print(word_count("jedin, k okok,"))