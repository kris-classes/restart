def graffiti():
    '''Does graffiti on wall'''
    print('Anything at all...')
    return 123

def clean():
    raise MyError

class MyError(Exception):
    pass
