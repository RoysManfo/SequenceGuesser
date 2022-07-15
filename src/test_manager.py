import test_check
import test_1_linear

import colorama
colorama.init()
from colorama import Fore

passed = 0

"""
Test Check
"""
if test_check.test_leght():
    print(Fore.GREEN + "O Test 1 passed")
    passed += 1
else:
    print(Fore.RED + " X Test 1 failed")

if test_check.test_is_list():
    print(Fore.GREEN + "O Test 2 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 2 failed")

if test_check.test_int_type():
    print(Fore.GREEN + "O Test 3 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 3 failed")


"""
Test 1 Linear
"""
if test_1_linear.test_linear_pattern():
    print(Fore.GREEN + "O Test 4 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 4 failed")

if test_1_linear.test_linear_pattern_2():
    print(Fore.GREEN + "O Test 5 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 5 failed")

if test_1_linear.test_even_num_pattern():
    print(Fore.GREEN + "O Test 6 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 6 failed")

if test_1_linear.test_even_num_pattern_2():
    print(Fore.GREEN + "O Test 7 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 7 failed")

if test_1_linear.test_odd_num_pattern():
    print(Fore.GREEN + "O Test 8 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 8 failed")

if test_1_linear.test_odd_num_pattern_2():
    print(Fore.GREEN + "O Test 9 passed")
    passed += 1
else:
    print(Fore.RED + "X Test 9 failed")




"""
RESULTS
"""
print("\n" + Fore.GREEN + "Passed: " + str(passed) + "/9")
print(Fore.GREEN + "Passed: " + str(float(passed / 9*100)) + "%")
