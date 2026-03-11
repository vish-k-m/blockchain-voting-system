import hashlib
import datetime

class Block:
    def __init__(self, voter, candidate, previous_hash):
        self.voter = voter
        self.candidate = candidate
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        data = str(self.voter) + str(self.candidate) + str(self.timestamp) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block("System", "Start", "0")
        self.chain.append(genesis)

    def add_vote(self, voter, candidate):
        previous_hash = self.chain[-1].hash
        block = Block(voter, candidate, previous_hash)
        self.chain.append(block)
