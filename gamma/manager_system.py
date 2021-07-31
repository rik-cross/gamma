class SystemManager:

    def __init__(self):
        self.systems = []
    
    def addSystem(self, system, *otherSystems):
        self.systems.append(system)
        for s in otherSystems:
            self.systems.append(s)
    
    def swap(self, s1, s2):
        self.systems[s1], self.systems[s2] = self.systems[s2], self.systems[s1]