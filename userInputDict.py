
class userInputDict:

    def __init__(self, chemDict):
        try:
            assert(isinstance(chemDict, dict))
            self.chemDict = chemDict
        except AssertionError:
            return False

    def getDictElement(self, idx):
        try:
            return self.chemDict[idx]
        except KeyError:
            return False

    def appendDictElement(self, value, order):
            self.chemDict[order] = value

    def deleteDictElement(self, idx):
        try:
            del self.chemDict[idx]
        except KeyError:
            return False

    def getDictLength(self):
        return len(self.chemDict)

    def clearDictElement(self):
        for key in self.chemDict.keys():
            del self.chemDict[key]