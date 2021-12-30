import gamma

class ScoreComponent(gamma.Component):

    def init(self):

        # component referred to as 'score'
        self.key = 'score'
        
        # component just holds a score, initially 0
        self.score = 0