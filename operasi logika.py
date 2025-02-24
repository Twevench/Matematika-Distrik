# Membuat jdul Tabel
print("TABEL KEBENARAN KONJUNGSI")
print("_________________________")

# #Menampilkan Header tabel
print("P\t|Q\t|P AND Q")
print("_________________________")
# Menggunakan Operator logika 'AND'
for P in [True, False]:
    for Q in [True, False]:
        konjungsi = P and Q
        print(f"{P}\t|{Q}\t{konjungsi}")
print()

# Menbuat jdul Tabel
print("TABEL KEBENARAN DISJUNGSI")
print("_________________________")

#Menampilkan Header tabel
print("P\t|Q\t|P AND Q")
print("_________________________")
# Menggunakan Operator logika 'AND'
for P in [True, False]:
    for Q in [True, False]:
        disjungsi = P or Q
        print(f"{P}\t|{Q}\t{disjungsi}")
print()

# Menbuat jdul Tabel
print("TABEL KEBENARAN NEGASI")
print("_________________________")

# #Menampilkan Header tabel
print("P\t|Q\t|P AND Q")
print("_________________________")
# Menggunakan Operator logika 'AND'
for P in [True, False]:
    for Q in [True, False]:
        negasi = not P or Q
        print(f"{P}\t|{Q}\t|{negasi}")
