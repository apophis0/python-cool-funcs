def input_strict(type, str):
    """Input only a certain type"""
    while True:
        try:
            x = type(input(str))
            return x
        except Exception:
            print(f"Please input the type: {type.__name__}")
