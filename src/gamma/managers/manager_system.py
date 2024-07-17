# stores all systems in a specified order
class SystemManager:

    def __init__(self):
        self.systems = []
    
    #def __str__(self):
    #    keyString = ''
    #    for s in self.systems:
    #        if s.key is not None:
    #            keyString += str(self.systems.index(s)) + ': ' + s.key + ' '
    #        else:
    #            keyString += str(self.systems.index(s)) + ': unknown '
    #    return keyString

    def addSystem(self, system, *otherSystems):
        self.systems.append(system)
        for s in otherSystems:
            self.systems.append(s)

    def moveFirst(self, systemKey):
        # find and remove system
        system = self._findSystem(systemKey, remove=True)
        # if system found, add to start of list
        if system is not None:
            self.systems = [system] + self.systems
    
    def moveLast(self, systemKey):
        # find and remove system
        system = self._findSystem(systemKey, remove=True)
        # if system found, add to end of list
        if system is not None:
            self.systems = self.systems + [system]

    def moveToPosition(self, systemKey, position):
        # find and remove system
        system = self._findSystem(systemKey, remove=True)
        # if system found, move to required position
        if system is not None:
            self.systems = self.systems[:position] + [system] + self.systems[position:]

    def moveBefore(self, systemKeyToMove, systemKey2):
        # find and remove system to move
        system = self._findSystem(systemKeyToMove, remove=True)
        # find position to move to (but don't remove)
        system2 = self._findSystem(systemKey2)
        # if system found, move to required position
        if system is not None and system2 is not None:
            moveIndex = self.systems.index(system2)
            self.systems = self.systems[:moveIndex] + [system] + self.systems[moveIndex:]
        
    def _findSystem(self, systemKey, remove=False):
        for s in self.systems:
            if s.key == systemKey:
                if remove:
                    self.systems.remove(s)
                return s
        return None
