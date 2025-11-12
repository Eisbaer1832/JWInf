import enum
import os
import unittest
import Silbentrennung as S
from loguru import logger


files = os.listdir("data/tasks")
logger.add("logs/automatic_testing_{time}.log", rotation="1 MB")

class Type:
    Task = "tasks"
    Solution = "solutions"

def load(fetch_type:Type, file):
    if fetch_type == Type.Task:
        with open('data/tasks/' + file) as f:
            return f.read()
    else:
        with open('data/solutions/' + file) as f:
            return f.read() + " "





def main():
    total = 0
    failed = 0

    for file in files:
        total = total + 1
        task = load(Type.Task, file)
        seperated = S.doSeperation(task)
        solution = " " + load(Type.Solution, file)
        if seperated == solution:
            logger.success(seperated.replace("\n", ""))
        else:
            logger.error(seperated.replace("\n", ""))
            failed = failed + 1

    logger.info(str(failed) + "/" + str(total) + " Tests fehlgeschlagen.")
    logger.info("Erfolgsquote: " + str(round((((total - failed) / total)*100),2)) + "%")

if __name__ == "__main__":
    main()