import sys
sys.path.append('/Users/work/OneDrive/Desktop/INVENTARIUM_BLOCK_CHAIN')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import  Blockheader
from Blockchain.Backend.utill.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
from Blockchain.Backend.core.Images.images import images
from Blockchain.Backend.utill.util import hash256

from pathlib import Path
from PIL import Image
import imagehash
import imagehash
import hashlib




import os
import time
import json

ZERO_HASH= '0'*64
VERSION=1


patho= Path("C:\\Users\\work\\OneDrive\\Desktop\\INVENTARIUM_BLOCK_CHAIN\\Blockchain\\Backend\\core\\Images\\Images_from_camera\\Signature.jpg")
pathi=Path("C:\\Users\\work\\OneDrive\\Desktop\\INVENTARIUM_BLOCK_CHAIN\\Blockchain\\Backend\\core\\Images\\images_from_camera")







class blockchain:
    def __init__(self,pathh):
        self.pathh=pathh
        self.files=os.listdir(self.pathh)
        self.GenesisBlock()


    def write_on_disk(self,block):
        blockchainDB= BlockchainDB()
        blockchainDB.write(block)
    
    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()


    def GenesisBlock(self):
        BlockHeight =0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def normalize_metadata(self,data):
        clean = {}

        for key, value in data.items():

            # convert key to string
            key = str(key)

            # convert bytes to hex
            if isinstance(value, bytes):
                value = value.hex()

            clean[key] = value

        return clean

    
    def dict_to_string(self,data):
        data=self.normalize_metadata(data)
        return json.dumps(data, sort_keys=True, separators=(',', ':'))
    
    def get_image_hash(self,image_path):
        try:
        # Load the image
           # img = Image.open(image_path)
        
        # Generate a Perceptual Hash (pHash)
        # This is resistant to slight resizing or color shifts
            with open(image_path, "rb") as f:
                hash_value=hashlib.sha256(f.read()).hexdigest()

        
            return hash_value
        
        except Exception as e:
            print(f"Error: {e}")

    def addBlock(self,BlockHeight,prevBlockHash,):

            for i in self.files:

                i=os.path.join(self.pathh,i)

                timestamp = int(time.time())
       
                transaction= self.get_image_hash(i)
                print(transaction)


                merkleRoot=hash256(str(transaction).encode()).hex()
                blockheader=Blockheader(VERSION,prevBlockHash,merkleRoot,0,'0')
                blockheader.mine()
                self.write_on_disk([Block(BlockHeight,1,blockheader.__dict__,1,str(transaction)).__dict__])
                print('BlockHeight is ', BlockHeight, 'prevBlockHash',prevBlockHash)
                print('                                                                 ')
                lastBlock=self.fetch_last_block() 

                BlockHeight=lastBlock["Height"]+1
                prevBlockHash=lastBlock['BlockHeader']['blockHash']
            print('BlockHeight is ', BlockHeight, 'prevBlockHash',prevBlockHash)
         




    def main(self):
            pass


files=os.listdir(pathi)

if __name__ == "__main__":
        bc=blockchain(pathi)
        bc.main()
     