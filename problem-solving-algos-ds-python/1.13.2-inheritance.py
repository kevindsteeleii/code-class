class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class UnaryGate(LogicGate):
  
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        return(int(input('Enter Pin Input for gate {}---> '.format(self.getLabel()))))


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input('Enter Pin A Input for gate {}---> '.format(self.getLabel()))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input('Enter Pin A Input for gate {}---> '.format(self.getLabel()))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):
    def __init__(self, n):
        super(NorGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 0
        else:
            return 1

class NandGate(BinaryGate):
    def __init__(self,n):
        super(NandGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        return 1 if pin==0 else 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
    g1 = AndGate('G1')
    g2 = OrGate('G2')
    g3 = NotGate('G3')
    # c1 = Connector(g1, g2)
    c2 = Connector(g3, g2)
    # c3 = Connector(g1, g2)
    print(g2.getOutput())

if __name__ == '__main__':
    main()

