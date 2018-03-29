from math import sqrt

class State:
    def __init__(self, table=[]):
        self.__table = table
        self.__size = len(table)

    def setCell(self, i, j, value):
        self.__table[i][j] = value
        return self

    def getCell(self, i, j):
        return self.__table[i][j]

    def getSize(self):
        return self.__size

    def getTable(self):
        return self.__table

    def getFrequencies(self):
        fq = [[x,0] for x in range(self.__size + 1)]
        for line in self.__table:
            for v in line:
                if v != 0:
                    fq[v][1] += 1

        return fq

    def setTable(self, table):
        self.__table = table
        self.__size = len(table[0])

    def getPossibleValuesRow(self, i):
        aux = [[x,1] for x in range(1, self.__size + 1)]
        for j in range(self.__size):
            if self.__table[i][j] != 0:
                aux[self.__table[i][j] - 1][1] = 0
        result = []
        for value in aux:
            if value[1] != 0:
                result.append(value[0])

        return result

    def getPossibleValuesCol(self, j):
        aux = [[x,1] for x in range(1, self.__size + 1)]
        for i in range(self.__size):
            if self.__table[i][j] != 0:
                aux[self.__table[i][j] - 1][1] = 0
        result = []
        for value in aux:
            if value[1] != 0:
                result.append(value[0])

        return result

    def getPossibleValuesSquare(self, i, j):
        starti = (i//int(sqrt(self.__size))) * int(sqrt(self.__size))
        startj = (j//int(sqrt(self.__size))) * int(sqrt(self.__size))

        aux = [[x,1] for x in range(1, self.__size + 1)]
        for k in range(starti, starti + int(sqrt(self.__size))):
            for l in range(startj, startj + int(sqrt(self.__size))):
                if self.__table[k][l] != 0:
                    aux[self.__table[k][l] - 1][1] = 0
        result = []
        for value in aux:
            if value[1] != 0:
                result.append(value[0])

        return result

    def checkColumn(self, j):
        stack = []
        for line in self.__table:
            if line[j] != 0 and line[j] in stack:
                return False
            stack.append(line[j])
        return True

    def checkRow(self, i):
        stack = []
        for x in self.__table[i]:
            if x != 0 and x in stack:
                return False
            stack.append(x)
        return True

    def checkSquare(self, startRow, startCol):
        stack = []
        n = int(sqrt(len(self.__table[0])))
        for i in range(startRow, startRow + n):
            for j in range(startCol, startCol + n):
                if self.__table[i][j] != 0 and self.__table[i][j] in stack:
                    return False
                stack.append(self.__table[i][j])
        return True

    def getFirstEmpty(self):
        for i in range(0, len(self.getTable())):
            for j in range(0, len(self.getTable())):
                if self.getTable()[i][j] == 0:
                    return i, j
        return -1, -1

    def __str__(self):
        result = ''
        for line in self.__table:
            for number in line:
                result = result + ' ' + str(number)
            result = result + '\n'
        return result