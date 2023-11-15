from tabulate import tabulate

def add_data(data_list):
    while True:
        answer = input("Mau menambah data? (y/t): ")
        if answer.lower() == 'y':
            nama = input("Masukkan nama: ")
            nim = input("Masukkan nim: ")
            nilai_tugas = int(input("Masukkan nilai tugas: "))
            nilai_uts = int(input("Masukkan nilai uts: "))
            nilai_uas = int(input("Masukkan nilai uas: "))
            nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
            data_list.append({'nama': nama, 'nim': nim, 'nilai_tugas': nilai_tugas, 'nilai_uts': nilai_uts, 'nilai_uas': nilai_uas, 'nilai_akhir': nilai_akhir})
        else:
            break
    return data_list

data_list = []
data_list = add_data(data_list)
headers = ['Nama', 'Nim', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir']
table_data = [(data['nama'], data['nim'], data['nilai_tugas'], data['nilai_uts'], data['nilai_uas'], data['nilai_akhir']) for data in data_list]
table_format = 'grid'
numalign = 'center'  # Center-align numeric columns
stralign = 'left'    # Left-align string columns
print(tabulate(table_data, headers=headers, tablefmt=table_format, numalign=numalign, stralign=stralign))
