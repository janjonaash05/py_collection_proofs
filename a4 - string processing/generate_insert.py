import re


def convert(username, text):
    pattern = re.compile(r'(.*[)]*\s*;)|(;\s*-{2})')
    username_injection = re.match(pattern, username)
    text_injection = re.match(pattern, text)
    if username_injection is None and text_injection is None:
        text = re.sub("((O[a-ž]*\s)?Mandík)|((A[a-ž]*\s)?Reichlová)|((J[a-ž]*\s)?Cimmrman)", "[CNZ]",text)
        return  f"INSERT INTO PRISPEVEK(AUTHOR,TEXT) values(\'{username}\',\'{text}\')"
    else:
        return "invalid"


if __name__ == '__main__':
    print(convert("Alena Reichlová", "Mandík a Jarek Cimmrman"))
