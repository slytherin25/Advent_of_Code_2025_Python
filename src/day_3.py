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
    def findLargestNumberInArray(self, numberArray: str) -> str:
        largestFound: int = -1
        for number in numberArray:
            if int(number) > largestFound:
                largestFound = int(number)

        return str(largestFound)

    #----------------------------------------------------------------------
    def findIndices(self, number: str, numberString: str) -> list[int]:
        indices: list[int] = []
        for index in range(len(numberString)):
            if numberString[index] == number:
                indices.append(index)

        return indices

    #----------------------------------------------------------------------
    def largest12DigitValue(self, numberString: str) -> str:

        answer: str = ""

        answerLength: int = 12

        aIndex: int = 0
        bIndex: int = len(numberString) - answerLength

        while bIndex < len(numberString):

            largestNumber: str = self.findLargestNumberInArray(numberString[aIndex:(bIndex + 1)])
            largestNumberIndices: list[int] = self.findIndices(largestNumber, numberString)

            for largestNumberIndex in largestNumberIndices:
                if aIndex <= largestNumberIndex <= bIndex:
                    aIndex = largestNumberIndex
                    break
            
            answer = answer + numberString[aIndex]

            aIndex = aIndex + 1
            bIndex = bIndex + 1

        return answer

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

        totalSum: int = 0
        for line in lines:
            largest12DigitValue: str = self.largest12DigitValue(line)
            totalSum = totalSum + int(largest12DigitValue)

        return totalSum
        