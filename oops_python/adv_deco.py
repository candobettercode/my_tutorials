def welcome():
    print("Welcome to the Advanced Decorators Tutorial!")

# welcome()

## CLOSURE EXAMPLE
def main_welcome():
    msg = "Welcome to the Advanced Decorators Tutorial!"
    def sub_welcom_class():
        print("Wel come to Mumbai")
        print(msg)
        print("This is a sub class of main_welcome")
    return sub_welcom_class()

# main_welcome()
def main_welcome_(func):
    def sub_welcom_class():
        print("Wel come to Mumbai")
        print("This is a sub class of main_welcome")
        func()
    return sub_welcom_class()

@main_welcome_
def welcome():
    print("Welcome to the Advanced Decorators Tutorial!")