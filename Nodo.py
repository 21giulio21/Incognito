

class Nodo:

    quasiIdentifier = []
    marked = False
    isRoot = False
    frequencySet = []
    levelOfGeneralizations = dict()


    def __init__(self,quasiIdentifier,marked, levelOfGeneralizations):
        self.quasiIdentifier = quasiIdentifier
        self.marked = marked
        self.parent = None
        self.levelOfGeneralizations = levelOfGeneralizations

    def calcoloFrequencySet(self):
        return [1,2,3]

    def setMarked(self,valore):
        self.marked = valore

    def description(self):
        print("*****dati nodo:*******")
        print("quasi Identifier:")
        print self.quasiIdentifier
        print("livelli di generalizzazione:")
        print self.levelOfGeneralizations
        print("*****fine dati nodo********\n\n")

