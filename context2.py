class SupressErrors:
    def __init__(self, *errors):
        self.errors = errors

    def __enter__(self):
        print("ENTER")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT')
        if exc_type is not None:
            if issubclass(exc_type, self.errors):
                print(f"exceptions {exc_type}")
                return True
        return False


try:
    with SupressErrors(ZeroDivisionError):
        x = 1 / 0
        print("123")
except Exception as exception:
    print(f"exception : {exception}")

try:
    with SupressErrors(ZeroDivisionError):
        x = 1 + '1'
except Exception as exception:
    print(f'exception : {exception}')
