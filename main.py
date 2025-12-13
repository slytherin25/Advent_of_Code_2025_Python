from typing import Any

from src.day_1 import Day1
from src.day_2 import Day2
from src.day_3 import Day3


def printAnswers(dayIndex: int, answers: list[Any]):
    print(f"#------------------Day {dayIndex} Solutions------------------#")
    for index in range(len(answers)):
        print(f'Answer {index}: {answers[index]}')
    print("")

#----------------------------------------------------------------------
def main():

    # Day 1 answers.
    day1: Day1 = Day1()
    printAnswers(1, [day1.part1Answer(), day1.part2Answer()])

    # Day 2 answers.
    day2: Day2 = Day2()
    printAnswers(2, [day2.part1Answer(), day2.part2Answer()])

    # Day 3 answers.
    day3: Day3 = Day3()
    printAnswers(3, [day3.part1Answer(), day3.part2Answer()])


#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
