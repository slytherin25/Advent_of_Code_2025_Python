import sys


class Day3:

    def __init__(self):
        pass

    #----------------------------------------------------------------------
    def readLines(self, filepath: str) -> list[tuple[str,str]]:
        '''
        Get all of the lines in the text file.
        
        :param filepath: filepath for the data
        :return: list of tuples for first and second id.
        '''
        lines: list[str] = []
        with open(filepath, "r") as file:
            lines = [line.strip() for line in file]

        return lines

    #----------------------------------------------------------------------
    def findAllPairings(self, numberString: str) -> list[str]:
        '''
        Finds all of the two-digit numbers possible in the string.
        
        :param numberString: The string being analyzed.
        :return: All two digit numbers.
        '''
        pairings: list[str] = []
        for firstIndex in range(len(numberString)):
            if firstIndex + 1 == len(numberString):
                break
            for secondIndex in range(firstIndex + 1, len(numberString)):
                pairings.append(f"{numberString[firstIndex]}{numberString[secondIndex]}")
        
        return pairings
    
    #----------------------------------------------------------------------
    def largest12DigitValue(self, numberString: str) -> str:

        return 0
    
    #----------------------------------------------------------------------
    def part1Answer(self):

        lines: list[str] = self.readLines("data/day_3_data.txt")

        totalSum: int = 0
        for line in lines:
            pairings: list[str] = self.findAllPairings(line)
            
            largestNumber: int = int(pairings[0])
            for pairing in pairings:
                if int(pairing) > largestNumber:
                    largestNumber = int(pairing)
            
            totalSum = totalSum + largestNumber

        return totalSum

    #----------------------------------------------------------------------
    def part2Answer(self):

        lines: list[str] = self.readLines("data/day_3_data.txt")
        lines=["1234"]

        totalSum: int = 0
        for line in lines:
            largest12DigitValue: str = self.largest12DigitValue(line)
            totalSum = totalSum + int(largest12DigitValue)

        return totalSum
        