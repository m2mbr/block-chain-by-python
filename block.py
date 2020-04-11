from datetime import datetime
import hashlib

class Block:
    
    def __init__(self, timeStamp, previousHash, data):
        self.index = 0
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.data = data
        self.hash = ""
        self.nonce = 0
        
    def calculate_hash(self):
        data = str(self.timeStamp) + str(self.previousHash) + str(self.data) + str(self.nonce)
        #print(data)
        result = hashlib.sha256(data.encode())
        return result.hexdigest()
        
    def block(self):
        self.hash = self.calculate_hash()
        
    def mine(self, difficulty):
        leadingZeros = ''
        for i in range(difficulty):
            leadingZeros += "0"

        while self.hash == None or self.hash[0:difficulty] != leadingZeros:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(self.nonce)


        
if __name__=='__main__':
    b = Block(timeStamp=datetime.now(), previousHash=None, data="{sender:Akash,receiver:Ovi,amount:10}")
    # b.block()
    # print(b.hash)
    
    b.mine(2)

    print(b.nonce, b.hash)
