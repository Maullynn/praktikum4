A = [10, 20, 30, 40, 50]
print("Elemen ke 3:", A[2]) 
print("Nilai elemen ke 2 sampai 4:", A[1:4]) 
print("Elemen terakhir:", A[-1])
A[3] = 999 
print("Elemen ke 4 setelah diubah:", A[3]) # 
A[3:] = [888, 777, 666] 
print("Elemen list setelah diubah:", A) 
B = A[:2] 
print("List B sebelum ditambahkan:", B)
B.append("baru") # Menambahkan nilai string ke list B
print("List B setelah ditambahkan nilai string:", B) # List B setelah ditambah