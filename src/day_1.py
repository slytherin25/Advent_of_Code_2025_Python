
class Day1:

    modulo: int = 100

    def __init__(self):
        pass

    #----------------------------------------------------------------------
    def readLines(self, filepath: str) -> list[tuple[str,int]]:
        '''
        Get all of the lines in the text file.
        
        :param filepath: filepath for the data
        :return: list of tuple with direction and tick counts
        '''
        lines: list[tuple[str,int]] = []
        with open(filepath, "r") as file:
            lines = [(line.strip()[0], int(line.strip()[1:])) for line in file]
        return lines
    
    #----------------------------------------------------------------------
    def adjustDial(self, currentIndex: int, direction: str, numTicks: int) -> int:
        '''
        Adjusts the dial.
        
        :param currentIndex: The current position on the dial.
        :param direction: The direction to move on the dial.
        :param numTicks: The number of tic ks to adjust by.
        :return: The new position on the dial.
        '''
        if direction.lower() == "r":
            currentIndex = (currentIndex + numTicks) % self.modulo
        else:
            currentIndex = (currentIndex - numTicks) % self.modulo

        return currentIndex

    #----------------------------------------------------------------------
    def part1Answer(self):

        lines: list[tuple[str,int]] = self.readLines("data/day_1_data.txt")

        zeroCount: int = 0

        currentIndex: int = 50 # starting point
        for line in lines:
            direction: str = line[0]
            numTicks: int = line[1]
            currentIndex = self.adjustDial(currentIndex, direction, numTicks)
            
            # Count how many times 0 is landed on.
            if currentIndex == 0:
                zeroCount = zeroCount + 1

        return zeroCount
    
    #----------------------------------------------------------------------
    def part2Answer(self):

        lines: list[tuple[str,int]] = self.readLines("data/day_1_data.txt")

        zeroCount: int = 0

        currentIndex: int = 50 # starting point
        for line in lines:
            direction: str = line[0]
            numTicks: int = line[1]

            for _ in range(numTicks):
                currentIndex = self.adjustDial(currentIndex, direction, 1)
                if currentIndex == 0:
                    zeroCount = zeroCount + 1

        return zeroCount
    