import copy


class Mock:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.original_attrs = {}
        self.temporary_attrs = kwargs

    def __enter__(self):

        for attr in self.temporary_attrs:

            if hasattr(self.obj, attr):
                self.original_attrs[attr] = copy.deepcopy(getattr(self.obj, attr))

        for attr, value in self.temporary_attrs.items():
            setattr(self.obj, attr, value)

        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):

        for attr, value in self.original_attrs.items():
            setattr(self.obj, attr, value)

        mock_attrs = set(self.temporary_attrs.keys())
        exist_attrs = set(self.original_attrs.keys())
        added_attrs = mock_attrs - exist_attrs
        for attr in added_attrs:
            delattr(self.obj, attr)

        return False


class User:
    def __init__(self):
        self.name = 'Name'
        self.balance = 999

    def __str__(self):
        return f'User:{self.name} Balance:{self.balance}'


user = User()
print(f"Initial: {user}")

with Mock(user, name='new_Name', balance=111, attr='1'):
    print(f"Mocked:  {user}")
    # This line now works and prints 'Mock attrs : 1'
    print(f'Mock attrs : {user.attr}')

print(f"Restored: {user}")
try:
    print(user.attr)
except AttributeError as e:
    print("Verified: user.attr was cleaned up.")
