def input_strict(allowed_types: list, prompt=None):
    """Input only (a) certain type(s)"""
    while True:
        x = input(prompt)
        for allowed in allowed_types:
            try:
                return allowed(x)
            except Exception:
                pass
        print("Please input something castable to one of the following:\n", ", ".join([type.__name__ for type in allowed_types]))

def main():
    # Test
    print("Testing: input_strict()")
    for allowed in (int, float, list, bool):
        foo = input_strict([allowed], "Input something castable to " + allowed.__name__ +": ")
        print(foo, "is a valid", allowed.__name__)
    return

if __name__ == "__main__":
    main()
   

#hello this is a pull request
#i am le oni simp
#how ya doin
