
import json
from hashlib import sha256

class Block:

    def __init__(self, index, payload: any, timestamp, prevBlockHash):
        self.prevBlockHash = prevBlockHash
        self.nonce = 0
        self.index = index
        self.payload = payload
        self.timestamp = timestamp

    def increaseNonce(self):
        self.nonce += 1
    @property
    def stringifyBlock(self):
        return json.dumps(self.__dict__, sort_keys=True)

    @property
    def hashMe(self):
        return sha256(self.stringifyBlock.encode()).hexdigest()

