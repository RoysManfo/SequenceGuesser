import main

def test_leght():
    try:
        main.check([])
        return False
    except ValueError:
        return True

def test_is_list():
    try:
        main.check((1,2,3,4,5))
        return False
    except TypeError:
        return True
    
def test_int_type():
    try:
        main.check(["1","2","3","4","5","6","7","8","9","10"])
        return False
    except TypeError:
        return True

