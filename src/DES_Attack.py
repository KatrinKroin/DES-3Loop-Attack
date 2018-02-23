from General_functions import *
from DES import *

def AttackPC1(bits):
    temp=[] 
    
    i=0
    while i<64:
        temp+='x'
        i+=1    
        
    pc=[57,   49,    41,   33,    25,    17,    9,
        1,   58,    50,   42,    34,    26,   18,
        10,    2,    59,   51,    43,    35,   27,
        19,   11,     3,   60,    52,    44,   36,
        63,   55,    47,   39,    31,    23,   15,
        7,   62,    54,   46,    38,    30,   22,
        14,    6,    61,   53,    45,    37,   29,
        21,   13,     5,   28,    20,   12,    4]
    
    i=0
    for bit in bits:
        place=pc[i]
        temp[place-1]=bit
        i+=1
    return "".join(temp)
       
def AttackPC2(bits): 
    temp=[] 
    
    i=0
    while i<56:
        temp+='x'
        i+=1    
        
    pc=[14,    17,  11,    24,     1,    5,
        3,     28,   15,     6,    21,   10,
        23,    19,   12,     4,    26,    8,
        16,     7,   27,    20,    13,    2,
        41,    52,   31,    37,    47,   55,
        30,    40,   51,    45,    33,   48,
        44,    49,   39,    56,    34,   53,
        46,    42,   50,    36,    29,   32]
    
    
    i=0
    for bit in bits:
        place=pc[i]
        temp[place-1]=bit
        i+=1
    return "".join(temp)
    
def AttackE(bits): 
    temp=[] 
    
    i=0
    while i<32:
        temp+='x'
        i+=1    
        
    e=[32,     1,     2,     3,     4,     5,
        4,     5,     6,     7,     8,     9,
        8,     9,     10,    11,    12,    13,
        12,    13,    14,    15,    16,    17,
        16,    17,    18,    19,    20,    21,
        20,    21,    22,    23,    24,    25,
        24,    25,    26,    27,    28,    29,
        28,    29,    30,    31,    32,    1]
    
    i=0
    for bit in bits: #len 48
        place=e[i]
        temp[place-1]=bit
        i+=1
    
    return "".join(temp)
        
def ReverseS1(bits):
    s=[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    

    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key  
    
    num=int(bits,2) 
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS2(bits):
    s=[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]


    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key
    num=int(bits,2)
         
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS3(bits):
    s=[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]


    
   
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    num=int(bits,2)
            
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS4(bits):
    s=[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    
    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    num=int(bits,2)
            
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS5(bits):
    s=[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    
    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    num=int(bits,2)
            
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 
        
def ReverseS6(bits):
    s=[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]


    
    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    num=int(bits,2)
            
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS7(bits):
    s=[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]


    
   
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    
    num=int(bits,2)       
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key 

def ReverseS8(bits):
    s=[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    
    
    key=[]
    i=0
    while i<6:
        key+='x'
        i+=1
    if 'x' in bits:
        return key 
    num=int(bits,2)
            
    options=[]   
    k=0
    q=0
    for i in s:
        for j in i:
            if j==num:
                row=(bin(k)[2:].zfill(2))  
                colomn=(bin(q)[2:].zfill(4)) 
                temp=''
                temp=[row[0]+colomn[0:4]+row[1]]
                options+=temp
            q+=1
        k+=1
        q=0
    
    i=0
    while i<6 :
        if options[0][i]==options[1][i] and options[0][i]==options[2][i] and options[0][i]==options[3][i]:
            key[i]=options[0][i]
        i+=1

    return key

def attackS5(bits,key):
    bits=E(bits)    
    result=''
    i=0
    temp = bits[24:30]
    while i<6:
        if temp[i] == key[i]:
            result+='0'
        else:
            result+='1'
        i+=1        
    output=S5(result)
    return XOR(XOR(output[0],output[1]),XOR(output[2],output[3]))
 
def commonbits(bits1,bits2):    
    result=bits1
    i=0   
    while i < len(bits1):
        if bits1[i]=='x'and bits2[i]!='x':
            result=result[:i]+bits2[i]+result[i+1:] 
        elif bits2[i]=='x'and bits1[i]!='x':
            result=result[:i]+bits1[i]+result[i+1:]
        elif bits2[i]==bits1[i]:   
            result=result[:i]+bits1[i]+result[i+1:]
        else: #error                       
            return -1            
        i+=1           
    return result    
