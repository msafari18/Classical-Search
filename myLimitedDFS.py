class LIMITED_DFS:
    def __init__(self, problem , limit ):
        self.f = []
        self.e = []
        self.problem = problem
        self.f.append(problem.start)

        self.path = []
        self.expand = []
        self.visited = []
        self.maxMemory = 0
        self.limit = limit

    def limitedDFSSearch(self, s,l):

        if l >= self.limit :
            return

        if len(self.f) + len(self.e) > self.maxMemory :
                self.maxMemory = len(self.f) + len(self.e)
        self.f.remove(s)
        self.e.append(s)

        actions = self.problem.actions(s)
        n = []

        for i in actions:
            if self.problem.result(s, i) not in n :
                n.append(self.problem.result(s, i))

        for i in n:

            if self.problem.goal_test(i) :
                # print('limit',l + 1)
                self.path.append(i)
                self.path.append(s)
                print ("finish")
                return True
            else :
                if (i not in self.f) and (i not in self.e) :
                    self.visited.append(i)
                    self.f.append (i)
                    m = self.dfsSearch(i)
                    if m == True:
                        self.path.append(s , l + 1)
                        return True
                    return False
        self.expand = self.e