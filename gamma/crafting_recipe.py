
class CraftingRecipe:

    def __init__(self,
    
        outputEntityString,
        input, *moreInputs
    
    ):

        self.output = outputEntityString

        self.inputs = []
        for i in [input] + list(moreInputs):
            self.inputs.append(i)
    
    def addInput(self, input):
        self.inputs.append(input)