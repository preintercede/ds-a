''' Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6). 

Input: num = 9669
Output: 9969

Input: num = 9996
Output: 9999

'''


class Solution:
    def maximum69Number(self, num: int) -> int:
        # convert nums to string
        str_num = str(num)
        # convert the string to a list
        list_num = list(str_num)

        # loop through the list and if the first number is a 6, turn it into a 9
        for i in range(len(str_num)):
            if list_num[i] == '6':
                list_num[i] = '9'
                break

        nums = ''.join(list_num)

        # convert it back to an integer
        return int(nums)
