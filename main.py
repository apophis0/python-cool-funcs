#hello im oni simp
def input_strict(allowed_types, str):
    """Input only (a) certain type(s)"""
    while True:
        x = input(str)
        for type in allowed_types:
            try:
                x = type(x)
                return x
            except Exception:
                pass
        print("Please input something castable to one of the following:\n",
              ", ".join([type.__name__ for type in allowed_types]))
