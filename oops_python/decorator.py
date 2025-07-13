def greet(fx):
    def mfx(*args, **kwargs):
        print("Greeting the function")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


def add(x, y):
    print(x + y)

@greet
def hello():
    print("Hello, World!")

# hello()
# greet(add)(2, 3)

