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
    return True if main.guess([10,9,8,7,6]) == [5,4,3,2,1] else False

def test_linear_pattern_2():
    return True if main.guess([5,4,3,2,1]) == [0,-1,-2,-3,-4] else False
