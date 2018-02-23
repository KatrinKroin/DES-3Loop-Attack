def binnumgenerator(word):
    MaxSizeBin=word.count('x');
    for Number in range(0,2**MaxSizeBin):
        Full = list(word)
        BinaryNumber="{0:0{Fill}b}\n".format(Number,Fill=MaxSizeBin);
        BinaryIndex = 0
        
        for Index in range(len(Full)):
            if Full[Index] == 'x':
                Full[Index] = BinaryNumber[BinaryIndex];
                BinaryIndex = BinaryIndex + 1              
                
        yield ''.join(Full)
        
def bruteforce(word,cypher,key):
    MaxSizeBin=key.count('x');
     
    for Number in range(0,2**MaxSizeBin):
        FullKey = list(key)
        BinaryNumber="{0:0{Fill}b}\n".format(Number,Fill=MaxSizeBin);
            
        BinaryIndex = 0
        
        for Index in range(len(FullKey)):
            if FullKey[Index] == 'x':
                FullKey[Index] = BinaryNumber[BinaryIndex];
                BinaryIndex = BinaryIndex + 1
                
        if(DES(word,"".join(FullKey)) == cypher):      
            print("KEY!!!!! ------>>    "+"".join(FullKey))
            return 0
        if(Number%10000==0):
            print("I reached: " + "".join(FullKey))