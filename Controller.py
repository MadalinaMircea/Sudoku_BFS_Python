class Controller:
    def __init__(self, instance):
        self.__instance = instance

    def getInstance(self):
        return self.__instance

    def setInstance(self, instance):
        self.__instance = instance

    def orderStates(self, states):
        pass

    def bfs(self, problem):
        q = [problem.getInitialState()]
        visited = []

        i = 0
        while q:
            state = q.pop()
            i = i + 1

            if problem.isSolution(state):
                return state, i

            if str(state) not in visited:
                visited.append(str(state))
                q.extend(problem.expand(state))

        return None, i

    def gbfs(self, problem):
        q = [problem.getInitialState()]
        visited = []

        i = 0
        while q:
            state = q.pop()
            i = i + 1

            if problem.isSolution(state):
                return state, i

            if str(state) not in visited:
                visited.append(str(state))
                q.extend(sorted(problem.expand(state), key=lambda x : problem.heuristic(state, x)))

        return None, i
