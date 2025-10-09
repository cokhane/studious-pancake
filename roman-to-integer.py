class Solution:
    @staticmethod
    def give_roman_values(roman_char):
        print(roman_char)
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000}
        return roman_numerals.get(roman_char,"?")

    def romanToInt(self, s: str) -> int:
        convert_to_list = list(s)

        new_list = [self.give_roman_values(item) for item in convert_to_list]
        new_item = 0
        new_list_length = len(new_list)

        print(new_list)
        for item in range(0,new_list_length):
            print('new_list[item] 1: ', new_list[item])

            print('item:', item)
            if item < new_list_length - 1 and new_list[item] < new_list[item+1]:
                print('new_list[item]: ', new_list[item])
                print('new_list[item-1]: ', new_list[item-1])
                new_item -= new_list[item]
            else:
                new_item += new_list[item]

        return new_item


forTest = Solution()

# LVIII
#
# 50 5 1 1 1
# 50 + 5

print(forTest.romanToInt('LVIII'))

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
# 1000 -100 1000 -10 100 -1 5


'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:


50 + 5 + 3 

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


1000 -100 1000 -10 100 -1 5

best solution

class Solution(object):
     def romanToInt(self, s):
        sum = 0
        prevValue = 0
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for c in s:
            currentValue = value[c]
            sum += (currentValue - 2 * prevValue) if (currentValue > prevValue) else currentValue
            prevValue = currentValue
        return sum

'''