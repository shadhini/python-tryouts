# Handle all the exception!

actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        return "Cleese"


if __name__ == '__main__':
    # Test code
    get_last_name()
    print("All exceptions caught! Good job!")
    print("The actor's last name is %s" % get_last_name())