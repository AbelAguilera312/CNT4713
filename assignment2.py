import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, current_year): 
        age = current_year - self.year
        print(f'Your age is {age}')

    def listAnniversaries(self):
        current_year = 2022
        anniversaries = [i for i in range(10, current_year - self.year + 1, 10)]
        return anniversaries

    def modifyYear(self, n):
        yearStr = str(self.year)
        modifiedStr = yearStr[:2] * n 
        combinedNum = self.year * n 
        combinedStr = str(combinedNum)
        newStr = ""
        for x in range(len(combinedStr)):
            if x % 2 == 0:
                newStr = newStr + combinedStr[x]
        modifiedStr = modifiedStr + newStr
        
        return modifiedStr

        
    @staticmethod
    def checkGoodString(string):
        digits_count = sum(c.isdigit() for c in string)

        return len(string) >= 9 and string[0].isalpha() and digits_count == 1

        
        
    

    @staticmethod
    def connectTcp(host, port):
        try:
            socket.create_connection((host, port))
            return True
        except:
            return False


