# stores all systems in a specified order
class SystemManager:

    def __init__(self):
        self.systems = []
    
    def addSystem(self, system, *otherSystems):
        self.systems.append(system)
        for s in otherSystems:
            self.systems.append(s)

    def moveFirst(self, systemKey):
        # find and remove system
        system = self._findandRemoveSystem(systemKey)
        # if system found, add to start of list
        if system is not None:
            self.systems = [system] + self.systems
    
    def moveLast(self, systemKey):
        # find and remove system
        system = self._findandRemoveSystem(systemKey)
        # if system found, add to end of list
        if system is not None:
            self.systems = self.systems + [system]

    def moveToPosition(self, systemKey, position):
        # find and remove system
        system = self._findandRemoveSystem(systemKey)
        # if system found, move to required position
        if system is not None:
            self.systems = self.systems[:position] + [system] + self.systems[position:]

    def _findandRemoveSystem(self, systemKey):
        for s in self.systems:
            if s.key == systemKey:
                self.systems.remove(s)
                return s
        return None
