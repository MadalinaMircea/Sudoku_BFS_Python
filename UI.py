class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def getCtrl(self):
        return self.__ctrl

    def setCtrl(self, ctrl):
        self.__ctrl = ctrl

    def mainMenu(self):
        x = input('1 - BFS\n2 - GBFS\nGive command: ')
        if x == '1':
            result, i = self.__ctrl.bfs(self.__ctrl.getInstance())
            print(result)
            print('Moves: ' + str(i))
        else:
            result, i = self.__ctrl.gbfs(self.__ctrl.getInstance())
            print(result)
            print('Moves: ' + str(i))