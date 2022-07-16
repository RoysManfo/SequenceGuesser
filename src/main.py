
def check(sequence:list) -> bool:
    # Check if the sequence is a list
    # If not, raise an error
    try:
        sequence.append(5)
        sequence.pop(-1)
    except Exception:
        raise TypeError("Sequence must be a list")
    
    # Check if the sequence is empty
    # If so, raise an error
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty")

    # Check if the sequence is a list of integers
    # If not, raise an error
    elif not all(isinstance(x, int) for x in sequence):
        raise TypeError("Sequence must be a list of integers")

    # Check if the sequence is a list of at least 5 integers
    # If not, raise an error
    elif len(sequence) < 5:
        raise ValueError("Sequence must be a list of at least 5 integers")

    else:
        return True

def start(sequence:list) -> list:
    """
    Guess the next 5 numbers of a sequecnce in a list.
    """
    check(sequence)
    return guess(sequence)

def guess(sequence:list) -> list:
    """
    Guess the next 5 numbers of a sequecnce in a list.
    """
    correlation = sequence[1] / sequence[0]
    print(correlation)
    is_right = True
    my_guess = []
    for i, j in enumerate(sequence):
        print(i, j)
        # if sequence[i] / sequence[i-1] != correlation:
        #     is_right = False
        #     break

    if is_right:
        for i in range(5):
            my_guess.append(int(sequence[i] * correlation))
        return my_guess

print(start([1,2,3,4,5]))
            