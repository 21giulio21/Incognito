

class Nodo:

    #Lista dei Quasi Identifier del nodo
    quasiIdentifier = []
    marked = False
    frequencySet = []

    def __init__(self,quasiIdentifier,marked):
        self.quasiIdentifier = quasiIdentifier
        self.marked = marked

    def calcoloFrequencySet(self):
        return [1,2,3]

    def setMarked(self,valore):
        self.marked = valore

    def descrizione(self):
        print "Marker del nodo "           + str(self.marked)
        print "quasi Identifier del nodo " + self.quasiIdentifier
        print "Frequency Set Del nodo"     +  self.frequencySet

