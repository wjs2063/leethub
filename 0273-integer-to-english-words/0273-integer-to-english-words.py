import sys 
from collections import defaultdict
sys.setrecursionlimit(10**7)
memo = defaultdict(str)
class Solution:

    one_digit_dict = {
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"
    }
    two_digit_dict = {
        10:"Ten",
        11:"Eleven",
        12:"Twelve",
        13:"Thirteen",
        14:"Fourteen",
        15:"Fifteen",
        16:"Sixteen",
        17:"Seventeen",
        18:"Eighteen",
        19:"Nineteen",
        20:"Twenty",
        30:"Thirty",
        40:"Forty",
        50:"Fifty",
        60:"Sixty",
        70:"Seventy",
        80:"Eighty",
        90:"Ninety"
        }

    def numberToWords(self, num: int) -> str:
        if num == 0 :return "Zero"
        if 1 <= num < 10:

            return self.one_digit_dict[num]

        
        elif 10 <= num < 20:
            return self.two_digit_dict[num]

        
        elif 20 <= num < 100:
            q,r = num // 10,num % 10
            return self.two_digit_dict[q * 10]+ ((" " + self.one_digit_dict[r]) if r else "" ) 

            
        elif 100 <= num < 1000:
            q,r = num // 100, num % 100
            return self.one_digit_dict[q] + " " + "Hundred" + ((" " +self.numberToWords(r)) if r else "" )

        elif 1000 <= num < 10 ** 6:
            q,r = num // 1000 ,num % 1000 
            return self.numberToWords(q) + " " + "Thousand" + ((" " + self.numberToWords(r)) if r else "" )
        elif 10 ** 6 <= num < 10 ** 9:
            q,r = num // 10**6, num % 10**6
            return self.numberToWords(q) + " " + "Million" + ((" " + self.numberToWords(r)) if r else "" )
        else:
            q,r = num // 10 ** 9, num % 10**9
            return self.numberToWords(q) + " " + "Billion" + ((" " + self.numberToWords(r)) if r else "" )
            
        

        