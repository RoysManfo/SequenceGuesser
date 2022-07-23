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
    if main.guess([0,2,4,6,8,10,12,14,16,18]) == [20,22,24,26,28]:
        return True
    else:
        return False

def test_odd_num_pattern():
    if main.guess([1,3,5,7,9]) == [11,13,15,17,19]:
        return True
    else:
        return False

def test_odd_num_pattern_2():
    if main.guess([1,3,5,7,9,11,13,15,17,19]) == [21,23,25,27,29]:
        return True
    else:
        print(main.guess([1,3,5,7,9,11,13,15,17,19]))
        return False
