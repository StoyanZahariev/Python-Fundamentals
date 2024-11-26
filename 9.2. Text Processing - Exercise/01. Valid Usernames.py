import re


def is_valid_username(username):
    if not (3 <= len(username) <= 16):
        return False

    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False

    if username != username.strip("-_"):
        return False

    return True


usernames = input().split(", ")

for username in usernames:
    if is_valid_username(username):
        print(username)
