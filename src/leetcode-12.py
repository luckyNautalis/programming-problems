# Problem 12: Integer to Romain

"""
Constraints:

1) 1 <= num <= 3999

"""

class Solution:

    numeral_dict = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",
                        50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

    def intToRoman(self, num: int) -> str:

        roman_numeral = ''
        for value in self.numeral_dict.keys():

           while(num >= value):

               num -= value
               roman_numeral += self.numeral_dict[value]

        return roman_numeral
