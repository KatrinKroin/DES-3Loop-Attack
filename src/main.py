from DES_Attack import *

import binascii
 
def main():
    Word="nonsense"
    WordB=''
    for i in Word:
        WordB+=(bin(ord(i))[2:].zfill(8))
    Output= bin(int('d8164228f290cbaf', 16))[2:].zfill(8)
    WordIP=IP(WordB)
    OutputFP=IP(Output)
    L0=WordIP[0:32]
    R0=WordIP[32:64]
    L3=OutputFP[0:32]
    R3=OutputFP[32:64] 
    

    keyORIGINAL= '0000000001xxxxx001xxxxx001xxxxx001xxxxx001xxxxx001xxxxx001xxxxx0'     

    
    key=list(PC1(keyORIGINAL)) #56 bits key out of 64
    keyL=key[0:28]
    keyR=key[28:56]
    
    K1=PC2(shift(keyL,1)+shift(keyR,1))
    K2=PC2(shift(keyL,2)+shift(keyR,2))
    K3=PC2(shift(keyL,4)+shift(keyR,4))   

    F1result=F(R0,K1)
    R1F=XOR(F1result,L0)
 
    F3result=F(L3,K3)
    L2F=XOR(F3result,R3)

    
    R1=commonbits(L2F,R1F)
   
    F2result=F(R1,K2)
    L1F=XOR(F2result,R0)      

    F2out=XOR(R0,R3)
   
    Soutput=ReverseP(F2out)
    S1out=Soutput[0:4]
    S2out=Soutput[4:8]
    S3out=Soutput[8:12]
    S4out=Soutput[12:16]
    S5out=Soutput[16:20]
    S6out=Soutput[20:24]
    S7out=Soutput[24:28]
    S8out=Soutput[28:32] 
   
    k2_xor_R1E=''.join(ReverseS1(S1out)+ReverseS2(S2out)+ReverseS3(S3out)+ReverseS4(S4out)+ReverseS5(S5out)+ReverseS6(S6out)+ReverseS7(S7out)+ReverseS8(S8out))
    R1attack=AttackE(XOR(k2_xor_R1E, K2))
    R1=commonbits(R1, R1attack)
    if R1==-1: 
        print("dismatch! ")
        return 0
    
    keyatt=XOR(k2_xor_R1E, E(R1)) 
    K2=commonbits(K2, keyatt)
    if K2==-1: 
        print("dismatch! ")
        return 0
    
    T=(AttackPC2(K2))
    Kleft=T[0:28]
    Kright=T[28:]
    
    a=AttackPC1(reverse_shift(Kleft, 2)+reverse_shift(Kright,2))           
    keyORIGINAL=commonbits(keyORIGINAL,a )
    if keyORIGINAL==-1: 
        print("dismatch! ")
        return 0

    
         
    MyList=[]
    MyR=[]
    Options=GUESS5(keyORIGINAL)
    print("optional key templates: ")
    for j in Options:
        i=0
        keyORIGINAL=j
        myXOR='x1xxxxxx01xxxxx0xxx001xxx10xxxx001xxxx1xxxx0x1xx'
        while i<3:

            key=list(PC1(keyORIGINAL)) #56 bits key out of 64
            keyL=key[0:28]
            keyR=key[28:56]            
            K1=PC2(shift(keyL,1)+shift(keyR,1))
            K2=PC2(shift(keyL,2)+shift(keyR,2))
            K3=PC2(shift(keyL,4)+shift(keyR,4))   
        
            F1result=F(R0,K1)
            R1F=XOR(F1result,L0)
              
            F3result=F(L3,K3)
            L2F=XOR(F3result,R3) 
            
            R1=commonbits(L2F,R1F)
            if R1==-1: 
                break
            F2result=F(R1,K2)
            L1F=XOR(F2result,R0)
            if commonbits(L1F, L3)==-1:
                break      
                               
            #R1attack=AttackE(XOR(k2_xor_R1E, K2))
            R1attack=AttackE(XOR(myXOR,K2))

            R1=commonbits(R1, R1attack)
            if R1==-1: 
                break
    
            #keyatt=XOR(k2_xor_R1E, E(R1))
            keyatt=XOR(myXOR, E(R1))
            
            K2=commonbits(K2, keyatt)
            if K2==-1: 
                break          
            
            T=(AttackPC2(K2))
            Kleft=T[0:28]
            Kright=T[28:]
            
            a=AttackPC1(reverse_shift(Kleft, 2)+reverse_shift(Kright,2))           

            keyORIGINAL=commonbits(keyORIGINAL,a )
            if keyORIGINAL==-1: 
                break
            
            i+=1
       
        if i==3:
            print("new key:    "+keyORIGINAL)     
            MyList+=[keyORIGINAL] 
            MyR+=[R1]
     

    #Sbox 2 input : 0000x0 (XOR(K1,E(R0))) -> 2 options 
    #when we find that sbox 2 output is 0001 -> the input must be 000010-> we find:  K1[11]->1
    
    
    #for i in MyList:    
        #bruteforce(WordB, Output, i) 

    
    #example1()
    #example2()
   
   
    return 0

def example1():
    w='cocacola'
    k='iloveyou'   
    W=''
    K=''
    for i in k:
        K+=(bin(ord(i))[2:].zfill(8))    
    for i in w:
        W+=(bin(ord(i))[2:].zfill(8))
        
    print("Plaintext:  "+w)  
    print("Key:        "+k)    
 
    Out=DES(W,K)    
    print("Encryption: "+Out)    
    reverse=DESReverse(Out,K)    
    print("Decryption: "+reverse)
    
    n = int(W, 2)
    print(binascii.unhexlify('%x' % n)) 

def example2():
    w='nonsense'
    k='Incendio'   
    W=''
    K=''
    for i in k:
        K+=(bin(ord(i))[2:].zfill(8))    
    for i in w:
        W+=(bin(ord(i))[2:].zfill(8))
        
    print("Plaintext:  "+w)  
    print("Key:        "+k)    
 
    Out=DES(W,K)    
    print("Encryption: "+Out)    
    reverse=DESReverse(Out,K)    
    print("Decryption: "+reverse)
    
    n = int(W, 2)
    print(binascii.unhexlify('%x' % n)) 

def GUESS5(keyORIGINAL):
    
    Word="nonsense"
    WordB=''
    for i in Word:
        WordB+=(bin(ord(i))[2:].zfill(8))
    Output= bin(int('d8164228f290cbaf', 16))[2:].zfill(8)
    WordIP=IP(WordB)
    OutputFP=IP(Output)
    L0=WordIP[0:32]
    R0=WordIP[32:64]
    L3=OutputFP[0:32]
    R3=OutputFP[32:64] 
    
    
    tmp=''
    i=0
    while i<48:
        tmp+='x'
        i+=1
        
    k1 = []
    i=0
    j=0
    bin_i=""   
    temp=[]
    while i<64:
        temp+='x'
        i+=1    
    i=0


    while i<64: #nums from 000000 to 111111
        temp[i]=0
        bin_i+=(bin(i)[2:].zfill(6))
        
        S5out = attackS5(R0,bin_i)
        
        a=XOR(XOR(L0[2],L0[7]),XOR(L0[13],L0[24]))
        b=XOR(a,S5out)
        c=XOR(XOR(R3[2],R3[7]),XOR(R3[13],R3[24]))
        #d=XOR(c,L3[16]) 
                   
        if XOR(c,b) == '0':
            temp[i] = 1
            k1+=[tmp[:24] + "".join(bin_i) + tmp[30:]]
        bin_i = ""
        i+=1


    fin_k1 = []
    for i in k1:
        T=(AttackPC2(i))
        Kleft=T[0:28]
        Kright=T[28:]
        temp=AttackPC1(reverse_shift(Kleft, 1)+reverse_shift(Kright,1)) 
        fin_k1+=[temp]




    k3 = []
    i=0
    bin_i=""
    temp=[]
    while i<64:
        temp+='x'
        i+=1    
    i=0
    
    
    while i<64:
        temp[i]=0
        bin_i+=(bin(i)[2:].zfill(6))        
        S5out = attackS5(L3,bin_i)
        
        a=XOR(XOR(R3[2],R3[7]),XOR(R3[13],R3[24]))
        b=XOR(a,S5out)
        c=XOR(XOR(L0[2],L0[7]),XOR(L0[13],L0[24]))
        #d=XOR(c,R0[16])
        
        if XOR(c,b) == '0':    
            temp[i] = 1
            k3+=[tmp[:24] + "".join(bin_i) + tmp[30:]]
        bin_i = ""
        i+=1

    
    fin_k3 = []
    for i in k3:
        T=(AttackPC2(i))
        Kleft=T[0:28]
        Kright=T[28:]
        temp=AttackPC1(reverse_shift(Kleft, 1)+reverse_shift(Kright,4)) 
        fin_k3+=[temp]



    fin_KEY = []
    
    for i in fin_k1:
        for j in fin_k3:
            if commonbits(i, j)!=-1 and commonbits(keyORIGINAL, j)!=-1 and commonbits(i, keyORIGINAL)!=-1 and XOR(j[3],i[27])== '1':
                fin_KEY += [commonbits(commonbits(i, j),keyORIGINAL)]

    return fin_KEY 

main()