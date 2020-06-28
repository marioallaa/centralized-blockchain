from block import Block
import time

class Chain:

    def __init__(self):
        self.chain = []
        self.chainDifficulty = 3
        self.createFirstBlock()

    def createFirstBlock(self):
        b = Block(0, '', time.time(), '')
        self.chain.append(b)

    def sameLevelAs(self, b: Block):
        while not b.hashMe.startswith('0'*self.chainDifficulty):
            b.increaseNonce()
        return True

    @property
    def returnData(self):
        return [b.__dict__ for b in self.chain]

    def appendBlock(self, b: Block):
        if self.sameLevelAs(b) and b.prevBlockHash == self.lastNode.hashMe:
            self.chain.append(b)
            print(self.chain)
            return True
        return False

    def mine(self, payload: any):
        b = Block(
            index=self.lastNode.index+1,
            payload=payload,
            timestamp=time.time(),
            prevBlockHash=self.lastNode.hashMe)
        return self.appendBlock(b)


    @property
    def lastNode(self):
        return self.chain[-1]