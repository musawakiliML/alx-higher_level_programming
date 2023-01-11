#!/usr/bin/python3


if __name__ == "__main__":
    """
    Print all names defined in hidden_4 module.
    """
    import hidden_4

    hidden_names = dir(hidden_4)
    for hidden_name in hidden_names:
        if hidden_name[:2] != "__":
            print(hidden_name)
