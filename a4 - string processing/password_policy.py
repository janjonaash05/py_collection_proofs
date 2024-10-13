import re


def validate_username(username, password):
    general_rules = re.match("(?=.*[^a-zA-Z0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{10,}", password)

    if general_rules is None:
        return "failed at regex"

    for i in range(len(username)-3):
        if re.match(f".*({username[i:i+4]}).*", password) is not None:
            return "failed at sub"

    return True


if __name__ == '__main__':
    print(validate_username("AHOJa", "0.akkaaaHOJ"))
