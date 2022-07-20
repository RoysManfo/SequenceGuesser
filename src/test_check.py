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

