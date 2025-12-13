
class Day2:

    def __init__(self):
        pass

    #----------------------------------------------------------------------
    def readLines(self, filepath: str) -> list[tuple[str,str]]:
        '''
        Get all of the lines in the text file.
        
        :param filepath: filepath for the data
        :return: list of tuples for first and second id.
        '''
        lines: list[tuple[str,str]] = []
        with open(filepath, "r") as file:
            idsWithDashes: list[str] = file.readline().split(",")
            for idsWithDash in idsWithDashes:
                lines.append((idsWithDash.split("-")[0], idsWithDash.split("-")[1]))

        return lines

    #----------------------------------------------------------------------
    def containsRepeat(self, numberString: str) -> bool:
        '''
        Determines if a string contains repeats as defined by problem 1.
        
        :param numberString: The string being analyzed.
        :return: If the string contains repeats.
        '''
        if len(numberString) % 2 == 1:
            return False
        
        startIndex: int = 0
        endIndex: int = int(len(numberString) / 2)

        return numberString[startIndex:endIndex] == numberString[endIndex:]

    #----------------------------------------------------------------------
    def containsRepeatV2(self, numberString: str) -> bool:
        '''
        Determines if a string contains repeats as defined by problem 2.
        
        :param numberString: The string being analyzed.
        :return: If the string contains repeats.
        '''

        if len(numberString) == 1:
            return False
        
        currentNumDivisions: int = 2
        while currentNumDivisions <= len(numberString):
            substringList: list[str] = []
            stringLength: int = int(len(numberString) / currentNumDivisions)
            totalLengthAdded: int = 0
            while totalLengthAdded < len(numberString):
                substringList.append(numberString[totalLengthAdded:(totalLengthAdded + stringLength)])
                totalLengthAdded = totalLengthAdded + stringLength
            
            compareString: str = substringList[0]
            allMatch: bool = True
            for substring in substringList:
                if substring != compareString:
                    allMatch = False
                    break
            
            if allMatch:
                return True
            
            currentNumDivisions = currentNumDivisions + 1
        
        return False


    #----------------------------------------------------------------------
    def part1Answer(self):

        lines: list[tuple[str,str]] = self.readLines("data/day_2_data.txt")

        totalSum: int = 0
        for line in lines:
            firstId: str = line[0]
            secondId: str = line[1]

            currentId: int = int(firstId)
            while currentId <= int(secondId):
                if self.containsRepeat(str(currentId)):
                    totalSum = totalSum + int(currentId)
                currentId = currentId + 1

        return totalSum
    
    #----------------------------------------------------------------------
    def part2Answer(self):

        lines: list[tuple[str,str]] = self.readLines("data/day_2_data.txt")

        totalSum: int = 0
        for line in lines:
            firstId: str = line[0]
            secondId: str = line[1]

            currentId: int = int(firstId)
            while currentId <= int(secondId):
                if self.containsRepeatV2(str(currentId)):
                    totalSum = totalSum + int(currentId)
                currentId = currentId + 1

        return totalSum
