class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = format(int(date[0:4]), 'b')
        month = format(int(date[5:7]), 'b')
        day = format(int(date[8:]), 'b')

        result = f"{year}-{month}-{day}"
        return result