class Block:
    """
    Block is a storage container that stores transaction

    """
    def __init__(self,Height,Blocksize,Blockheader,TxCount, Txs):
        self.Height=Height
        self.Blocksize=Blocksize
        self.BlockHeader=Blockheader
        self.Txcount=TxCount
        self.Txs=Txs


