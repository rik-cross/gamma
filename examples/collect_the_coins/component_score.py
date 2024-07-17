import gamma

class ScoreComponent(gamma.Component):

    def init(self):
        
        # component just holds a score, initially 0
        self.score = 0