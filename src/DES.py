from General_functions import *

def PC1(bits):
    pc=[57,   49,    41,   33,    25,    17,    9,
        1,   58,    50,   42,    34,    26,   18,
        10,    2,    59,   51,    43,    35,   27,
        19,   11,     3,   60,    52,    44,   36,
        63,   55,    47,   39,    31,    23,   15,
        7,   62,    54,   46,    38,    30,   22,
        14,    6,    61,   53,    45,    37,   29,
        21,   13,     5,   28,    20,   12,    4]
    result=''
    for bit in pc:
        result+=bits[bit-1]
    return result

def PC2(bits):
    pc=[14,    17,  11,    24,     1,    5,
        3,     28,   15,     6,    21,   10,
        23,    19,   12,     4,    26,    8,
        16,     7,   27,    20,    13,    2,
        41,    52,   31,    37,    47,   55,
        30,    40,   51,    45,    33,   48,
        44,    49,   39,    56,    34,   53,
        46,    42,   50,    36,    29,   32]

    result=''
    for bit in pc:
        result+=bits[bit-1]
    return result

def shift(bits, num):
    return bits[num:]+bits[:num]

def reverse_shift(bits, num):
    return bits[-num:]+bits[:-num]  
    
def XOR(bits1,bits2):
    result=''
    i=0   
    while i < len(bits1):
        if bits1[i]!='x' and bits2[i]!='x':
            if bits1[i]==bits2[i]:
                result+='0'
            else:
                result+='1'
        else:
            result+='x'    
        i+=1
        
    return result
        
def F(bits,key):  # top-down
    bits=E(bits)
    result=XOR(bits,key)
    output=S1(result[0:6])+S2(result[6:12]) +S3(result[12:18])+S4(result[18:24])+S5(result[24:30])+S6(result[30:36])+S7(result[36:42])+S8(result[42:48])  
    result=P(output)
    return result

def IP(bits):
    ip=[58, 50, 42,    34,    26,    18,    10,    2,
        60,    52,    44,    36,    28,    20,    12,    4,
        62,    54,    46,    38,    30,    22,    14,    6,
        64,    56,    48,    40,    32,    24,    16,    8,
        57,    49,    41,    33,    25,    17,    9,    1,
        59,    51,    43,    35,    27,    19,    11,    3,
        61,    53,    45,    37,    29,    21,    13,    5,
        63,    55,    47,    39,    31,    23,    15,    7]
        
    result=''
    for bit in ip:
        result+=bits[bit-1]
    return result
        
def FP(bits):
    fp=[40,    8,    48,    16,    56,    24,    64,    32,
        39,    7,    47,    15,    55,    23,    63,    31,
        38,    6,    46,    14,    54,    22,    62,    30,
        37,    5,    45,    13,    53,    21,    61,    29,
        36,    4,    44,    12,    52,    20,    60,    28,
        35,    3,    43,    11,    51,    19,    59,    27,
        34,    2,    42,    10,    50,    18,    58,    26,
        33,    1,    41,    9,    49,    17,    57,    25]

    result=''
    for bit in fp:
        result+=bits[bit-1]
    return result

def P(bits):
    p=[16, 7, 20, 21, 
       29, 12, 28, 17, 
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]
    
    result=''
    for bit in p:
        result+=bits[bit-1]
    return result

def ReverseP(bits):
    temp=[]
    i=0
    while i<32:
        temp+='x'
        i+=1    
        
    p=[16, 7, 20, 21, 
       29, 12, 28, 17, 
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]
    
    i=0
    for bit in bits:
        place=p[i]
        temp[place-1]=bit
        i+=1
    return "".join(temp)

def E(bits):
    e=[32,    1,    2,    3,    4,    5,
        4,    5,    6,    7,    8,    9,
        8,    9,    10,    11,    12,    13,
        12,    13,    14,    15,    16,    17,
        16,    17,    18,    19,    20,    21,
        20,    21,    22,    23,    24,    25,
        24,    25,    26,    27,    28,    29,
        28,    29,    30,    31,    32,    1]

    result=''
    for bit in e:
        result+=bits[bit-1]
    return result

def S1(bits):

    s=[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output   
    
def S2(bits):
    s = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
         
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output     
         
def S3(bits):
    s = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output

def S4(bits):
    s = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output
    
def S5(bits):
    s = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
         
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output
    
def S6(bits):
    s = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
         
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output
    
def S7(bits):
    s = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
         
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output
    
def S8(bits):
    s = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
         
    result=''
    if 'x' not in bits:
        result=bits[0]+bits[5]
        return bin(s[int(result,2)][int(bits[1:5],2)])[2:].zfill(4)    
    else:
        arr=[]
        for i in binnumgenerator(bits):
            result=i[0]+i[5]
            arr+=[''.join(bin(s[int(result,2)][int(i[1:5],2)])[2:].zfill(4))]
        output=arr[0];  
        for i in arr:
            j=0
            while j<4:
                if i[j]!=output[j]:
                    output=output[:j]+'x'+output[j+1:]
                j+=1    
        return output
    
def DES(WordB,key):
    
    WordIP=IP(WordB)
    
    L0=WordIP[0:32]
    R0=WordIP[32:64]  
    
    key=list(PC1(key)) #56 bits key out of 64
    keyL=key[0:28]
    keyR=key[28:56]
    
    K1=PC2(shift(keyL,1)+shift(keyR,1))
    K2=PC2(shift(keyL,2)+shift(keyR,2))
    K3=PC2(shift(keyL,4)+shift(keyR,4))
    
    #Round 1
    Temp=F(R0,K1)
    R1=XOR(L0,Temp)
    L1=R0
    
    #Round 2
    Temp=F(R1,K2)
    R2=XOR(L1,Temp)
    L2=R1 
        
    #Round 3
    Temp=F(R2,K3)
    R3=XOR(L2,Temp)
    L3=R2
    
    result=L3+R3
    return FP(result)

def DESReverse(WordB,key):
        
    WordIP=IP(WordB)
    
    L0=WordIP[0:32]
    R0=WordIP[32:64]  
    
    key=list(PC1(key)) #56 bits key out of 64
    keyL=key[0:28]
    keyR=key[28:56]
    
    K3=PC2(shift(keyL,1)+shift(keyR,1))
    K2=PC2(shift(keyL,2)+shift(keyR,2))
    K1=PC2(shift(keyL,4)+shift(keyR,4))
    
    #Round 1
    Temp=F(R0,K1)
    R1=XOR(L0,Temp)
    L1=R0
    
    #Round 2
    Temp=F(R1,K2)
    R2=XOR(L1,Temp)
    L2=R1 
        
    #Round 3
    Temp=F(R2,K3)
    R3=XOR(L2,Temp)
    L3=R2
    
    result=L3+R3
    return FP(result)

