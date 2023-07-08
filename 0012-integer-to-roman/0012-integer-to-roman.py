class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        result = ""
        kept_key = ''
        while num > 0:
            for key, value in roman_map.items():
                if (num / value) >= 1:
                    kept_key = key
            while (num / roman_map[kept_key]) >= 1:
                result += kept_key
                num -= roman_map[kept_key]
        return result
        