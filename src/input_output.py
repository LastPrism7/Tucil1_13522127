import numpy as np
import os

def inputFile():
    filename=str(input("Masukkan Nama File:"))
    for root, dirs, files in os.walk(r'C:\Users\mauia'):
        for name in files:
            if name == filename:
                print(os.path.abspath(os.path.join(root, name)))

def inputOto():
    NToken = int(input("Masukkan Jumlah Token Unik:"))
    lenTemp = 0
    while (lenTemp != NToken):
        print("Masukkan Token:")
        ArrToken = list(map(str, input().split()))
        lenTemp = len(ArrToken)
    Buffer = int(input("Masukkan Ukuran Buffer:"))
    lenTemp = 0
    while (lenTemp != 2):
        print("Masukkan Ukuran Matrix:")
        DimensiMat = list(map(int, input().split()))
        lenTemp=len(DimensiMat)
    SumCQ = int(input("Masukkan Jumlah Sekuens:"))
    MaxCQ = int(input("Masukkan Ukuran Maksimal Sekuens:"))

def inputOptions():
    print("1. Input Dengan File")
    print("2. Input Otomatis")
    x=int(input("Ketik Nomor Pilihan yang diinginkan:"))
    if x==1:
        inputFile()
    elif x==2:
        inputOto()
    else:
        print("Opsi Tidak Valid.")
        inputOptions()

def Matrix_Rand(m,n,Arr):
    temp = np.random.randint(len(Arr), size=(m,n))
    res = np.empty((m,n), dtype='<U4')
    for i in range (0,m):
        for j in range (0,n):
            res[i][j]=Arr[temp[i][j]]
    return res

def CQ_Rand(n,Arr):
    temp = np.random.randint(len(Arr), size=(n))
    res = np.empty((n), dtype='<U4')
    for i in range (0,n):
        res[i]=Arr[temp[i]]
    return res

inputOptions()