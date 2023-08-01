# Odometer-

 This Python script provides functions to work with odometer numbers. Odometer numbers are positive integers with non-decreasing digits and do not contain the digit '0'. The code contains various utility functions to generate and manipulate these special numbers.
 
**Functions**

1. **is_ascending(n: int) -> bool:**
This function checks if the given integer n is an odometer number by examining whether its digits are in ascending order.

2. **no_zeros(n: int) -> bool:**
This function checks if the given integer n contains the digit '0' or not, returning True if there are no zeros in the number.

3. **is_odo_num(n: int) -> bool:**
This function determines if the given integer n is an odometer number by validating that it is both in ascending order and does not contain the digit '0'.

4. **all_odo_num(num_dig: int) -> list[int]:**
This function generates a list of odometer numbers containing a specific number of digits, given by the input num_dig.

5. **next_reading(n: int) -> int:**
This function finds the next odometer number following the input n.

6. **prev_reading(n: int) -> int:**
This function finds the previous odometer number before the input n.

7. **nth_reading_before(num: int, r: int) -> int:**
This function finds the nth odometer number before the input num, where n is given by r.

8. **nth_reading_after(num: int, r: int) -> int:**
This function finds the nth odometer number after the input num, where n is given by r.

9. **distance(a: int, b: int) -> int:**
This function calculates the distance between two odometer numbers, a and b. The distance is defined as the number of odometer numbers between a and b, inclusively.











