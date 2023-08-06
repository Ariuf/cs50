def announce(f):
    def wrapper():
        print('about to run a function')
        f()
        print('done with the function')
    return wrapper

@announce
def hello():
    print('hello world')
    