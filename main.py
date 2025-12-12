from typing import Any

from src.day_1 import Day1


def printAnswers(dayIndex: int, answers: list[Any]):
    print(f"#------------------Day {dayIndex} Solutions------------------#")
    for index in range(len(answers)):
        print(f'Answer {index}: {answers[index]}')
    print("")

#----------------------------------------------------------------------

def main():

    day1: Day1 = Day1()
    printAnswers(1, [day1.part1Answer(), day1.part2Answer()])


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()