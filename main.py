def input_strict(allowed_types: tuple, prompt=None):
    """Input only (a) certain type(s)"""
    while True:
        x = input(prompt)
        for type in allowed_types:
            try:
                return type(x)
            except Exception:
                pass
        print("Please input something castable to one of the following:\n", ", ".join([type.__name__ for type in allowed_types]))

def main():
    input_strict((int), "Input an int: ")
    return

if __name__ == "__main__":
    main()
