import numpy as np
import time
import os
from datetime import datetime

def inputFile():
    filename=str(input("Masukkan Nama File (Tanpa Extension): "))
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, '..', 'test', filename+'.txt')
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            Buffer = int(file.readline().strip())
            m, n = map(int, file.readline().strip().split())
            Matrix_File = []
            Arr_Token = set(Matrix_File)
            for _ in range(m):
                row = list(map(str, file.readline().strip().split()))
                Matrix_File.append(row)
            Sum_CQ = int(file.readline().strip())
            Arr_CQ = []
            Arr_CQ_Val = []
            for _ in range(Sum_CQ):
                Arr_CQ.append(file.readline().strip())
                Arr_CQ_Val.append(int(file.readline().strip()))
            DisplayMatrix(Matrix_File,m,n)
            for i in range(Sum_CQ):
                print(Arr_CQ[i])
                print(Arr_CQ_Val[i])
            Algoritma(Matrix_File,m,n,Buffer,Arr_Token,Arr_CQ,Arr_CQ_Val)
    else:
        print("File Tidak Ditemukan. ")
        inputFile()

def inputOto():
    NToken = int(input("Masukkan Jumlah Token Unik: "))
    lenTemp = 0
    while (lenTemp != NToken):
        print("Masukkan Token: ")
        Arr_Token = list(map(str, input().split()))
        SetToken = set(Arr_Token)
        if len(SetToken) == len(Arr_Token):
            lenTemp = len(Arr_Token)
            if lenTemp != NToken:
                print("Jumlah token tidak sesuai. ")
        else:
            print("Token harus unik. ")
    Buffer = int(input("Masukkan Ukuran Buffer: "))
    lenTemp = 0
    while (lenTemp != 2):
        print("Masukkan Ukuran Matrix: ")
        DimensiMat = list(map(int, input().split()))
        lenTemp=len(DimensiMat)
    SumCQ = 0
    while SumCQ<1:
        SumCQ = int(input("Masukkan Jumlah Sekuens: "))
        if SumCQ<1:
            print("Jumlah Harus Lebih Besar Daripada Nol. ")
    MaxCQ = 0
    while MaxCQ<1:
        MaxCQ = int(input("Masukkan Ukuran Maksimal Sekuens: "))
        if MaxCQ<1:
            print("Ukuran Harus Lebih Besar Daripada Nol. ")
    Arr_CQ = np.random.randint(1,MaxCQ+1, size=(SumCQ))
    Arr_CQ.sort()
    Arr_CQ_Val = np.random.randint(1,100, size=(SumCQ))
    Arr_CQ_Val.sort()
    Arr_CQ = ["" for x in range(SumCQ)]
    for i in range(SumCQ):
        Arr_CQ[i]=CQ_Rand(Arr_CQ[i],Arr_Token)
    Matrix_Hasil = Matrix_Rand(DimensiMat[0],DimensiMat[1],Arr_Token)
    DisplayMatrix(Matrix_Hasil,DimensiMat[0],DimensiMat[1])
    for i in range(SumCQ):
        print(Arr_CQ[i])
        print(Arr_CQ_Val[i])
    Algoritma(Matrix_Hasil,DimensiMat[0],DimensiMat[1],Buffer,Arr_Token,Arr_CQ,Arr_CQ_Val)

def inputOptions():
    print("1. Input Dengan File ")
    print("2. Input Otomatis ")
    x=int(input("Ketik Nomor Pilihan yang diinginkan: "))
    if x==1:
        inputFile()
    elif x==2:
        inputOto()
    else:
        print("Opsi Tidak Valid. ")
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
    res = Arr[temp[0]]
    for i in range (1,n):
        res+=' '
        res+=Arr[temp[i]]
    return res

def DisplayMatrix(Mat,m,n):
    for i in range(m):
        for j in range(n):
            print(Mat[i][j],end=" ")
        print()

def Algoritma(Mat,m,n,Buf,Token,CQ,CQ_Val):
    start_time = time.perf_counter()
    Solution = ''
    if max(CQ_Val)<=0:
        Solution = 'No Solution'
    else:
        print("temp")
    end_time = time.perf_counter()
    time_diff = round((end_time - start_time) * 1000)
    print(time_diff)

    Save_Prompt=str(input('Apakah Ingin Menyimpan Solusi? (Y/N) '))
    if Save_Prompt=='Y' or Save_Prompt=='y':
        current_time = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, '..', 'test', current_time + '.txt')
        with open(file_path, 'w') as file:
            file.write(Solution + '\n')
            file.write(str(time_diff) + " ms")
        print("Output Berhasil Disimpan.")
    else:
        print("Output Tidak Disimpan. ")

def Possible_Paths(m,n,Buffer,x,y,vertical):
    
    print("temp")
if __name__ == "__main__":
    inputOptions()
    #Possible_Paths(4,4,4,0)