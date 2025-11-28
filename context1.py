import copy


class TransactionalObjectSaver:
    def __init__(self,obj):
        self.obj = obj
        self.copy_data = None

    def __enter__(self):
        self.copy_data = copy.deepcopy(self.obj.__dict__)
        print('ENTER')
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception: {exc_val}")
            self.obj.__dict__.clear()
            self.obj.__dict__.update(self.copy_data)
            return False
        print("Succes")
        return True


class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"User:{self.name} Balance:{self.balance}"


def update(user : User,new_name,new_balance,error):
    user.name = new_name
    user.balance = new_balance
    if error:
        raise ValueError


user = User('Bob',1000)
print(f'{user}')
try:
    with TransactionalObjectSaver(user) as transactional_obj:
        update(transactional_obj,'John',999,True)
except ValueError as exception:
    print(f"Caught the exception {exception}")

user2 = User('Bob',1000)
print(f'{user2}')
try:
    with TransactionalObjectSaver(user2) as transactional_obj:
        update(transactional_obj,'John',999,False)
except ValueError as exception:
    print(f"Caught the exception {exception}")

print(f'{user2}')