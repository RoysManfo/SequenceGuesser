import main


def test_linear_pattern():
    if main.guess([1,2,3,4,5]) == [6,7,8,9,10]:
        return True
    else:
        return False

def test_linear_pattern_2():
    if main.guess([1,2,3,4,5,6,7,8,9,10]) == [11,12,13,14,15]:
        return True
    else:
        return False

def test_even_num_pattern():
    if main.guess([0,2,4,6,8]) == [10,12,14,16,18]:
        return True
    else:
        return False

def test_even_num_pattern_2():
    if main.guess([0,2,4,6,8,10,12,14,16,18]) == [20,22,24,26,28,30,32,34,36,38]:
        return True
    else:
        return False

def test_odd_num_pattern():
    if main.guess([1,3,5,7,9]) == [11,13,15,17,19]:
        return True
    else:
        return False

def test_odd_num_pattern_2():
    if main.guess([1,3,5,7,9,11,13,15,17,19]) == [21,23,25,27,29,31,33,35,37,39]:
        return True
    else:
        return False
