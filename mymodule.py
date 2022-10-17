def graffiti():
    print('Anything at all...')
    return 123

def clean():
    raise MyError

class MyError(Exception):
    pass

