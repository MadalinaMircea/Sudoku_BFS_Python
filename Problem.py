from math import sqrt
from copy import deepcopy
from State import State

class Problem:
    def __init__(self, initial):
        self.__initialState = initial
        self.readFromFile()

    def getInitialState(self):
        return self.__initialState

    def setInitialState(self, initial):
        self.__initialState = initial

    def heuristic(self, state1, state2):
        posi, posj = state1.getFirstEmpty()
        fq = self.__initialState.getFrequencies()
        value = state2.getCell(posi, posj)

        return fq[value][1]

    def expand(self, state):
        result = []
        i, j = state.getFirstEmpty()
        rowVals = state.getPossibleValuesRow(i)
        colVals = state.getPossibleValuesCol(j)
        sqVals = state.getPossibleValuesSquare(i, j)

        for v in rowVals:
            if v in colVals and v in sqVals:
                s = State(deepcopy(state.getTable()))
                s.setCell(i, j, v)
                result.append(s)

        return result


    def readFromFile(self):
        file = open('E:\Mada\E\School\IA\Sudoku\input3.in')
        table = []
        try:
            n = int(file.readline())
            for i in range(n):
                aux = []
                line = file.readline()
                line = line.split(' ')
                for v in line:
                    aux.append(int(v))
                table.append(aux)
            self.__initialState.setTable(table)
        except Exception as e:
            print(e)


    @staticmethod
    def isComplete(state):
        i, j = state.getFirstEmpty()
        if i >= 0:
            return False

        return True

    @staticmethod
    def isSolution(state):
        if not Problem.isComplete(state):
            return False

        for i in range(0, state.getSize()):
            if not state.checkRow(i) or not state.checkColumn(i):
                return False

        for i in range(0, state.getSize(), int(sqrt(state.getSize()))):
            for j in range(0, state.getSize(), int(sqrt(state.getSize()))):
                if not state.checkSquare(i, j):
                    return False

        return True