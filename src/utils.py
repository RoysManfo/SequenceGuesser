# GNU GPL Licence:
# Copyright (C) 2022  Roys Manfo

# This file is part of SeGu AI (Seqence Guesser Artificial Intelligence).

# SeGu AI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SeGu AI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SeGu AI.  If not, see <http://www.gnu.org/licenses/>.

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
        if not all(isinstance(x, float) for x in sequence):
            raise TypeError("Sequence must be a list of integers")

    # Check if the sequence is a list of at least 5 integers
    # If not, raise an error
    elif len(sequence) < 5:
        raise ValueError("Sequence must be a list of at least 5 integers")

    else:
        return True

def learn(cell) -> None:

    """
    When SeGu AI learns someting, it will save it in a file.
    """
    with open("SeGu.brain", "r") as f:
        if cell+"\n" not in f.readlines():
            with open("SeGu.brain", "a") as f:
                f.write(cell + "\n")
    return 

def remember() -> int:
    """
    SeGu AI will remember the sequence it learned by using it's brain file to get the equation
    of the sequence.
    """
    pass