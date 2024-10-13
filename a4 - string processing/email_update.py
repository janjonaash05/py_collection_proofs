import re


def validate_email(username, email):

    email_format_validation = re.match("^[\w\.]+@([\w]+\.)+[\w]{2,4}$", email)
    email_length_validation = re.match("^(.){6,100}$", email)
    username_length_validation = re.match("^(.*){4,100}$", username)

    if email_format_validation is not None and email_length_validation is not None and username_length_validation is not None:
        return f"UPDATE ACCOUNT SET email = {email} where username = {username}"
    else:
        raise ValueError("Error occurred. Invalid email or username format")


if __name__ == '__main__':
    print(validate_email("AHOJa", "testaaaaaaaa@gmail.comm"))
