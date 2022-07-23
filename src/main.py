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

from utils import check, learn

def start(sequence:list, NUM:int = 5) -> list:
    """
    Guess the next {NUM} numbers of a sequecnce in a list.
    """
    check(sequence)
    return guess(sequence, NUM)   

def guess(sequence:list, NUM:int=5) -> list:
    """
    Guess the next {NUM} numbers of a sequecnce in a list.
    The program will approach the problem by creating a graph of the sequence, where 
    X is the number of the sequence and Y is the index of that number.
    """
    is_right = True
    by_addiction = True
    cell = ''
    # SeGu will start by checking if the values of the numbers of sequence increase or decrease
    # If they increase, SeGu will guess the correlation could contain a + or *
    # If they decrease, SeGu will guess the correlation could contain a - or /

    if max(sequence) == sequence[-1] and min(sequence) == sequence[0]:
        increase = True
    elif max(sequence) == sequence[0] and min(sequence) == sequence[-1]:
        decrease = True

    if increase:
        correlation = sequence[1] - sequence[0]
    
        for i, j in enumerate(sequence):
            # print(i, j)
            if i == 0:
                continue
            elif j - sequence[i-1] != correlation:
                is_right = False
                by_addiction = False
                break

        if is_right and by_addiction:
            my_guess = [i for i in range(sequence[-1] + correlation, sequence[-1] + NUM * correlation + 1, correlation)]
            cell = f"x + {correlation}"
            learn(cell)

    elif decrease:
        pass
    else:
        return ["No correlation detected"]
    return my_guess

# print(start([10, 20, 30, 40, 50], 5))
            