from Queue_other import QueueData
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTesk = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTesk != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTesk = None

    def busy(self):
        if self.currentTesk != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTesk = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = QueueData()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


def newPrintTask():

    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(100):
        simulation(36000, 3)