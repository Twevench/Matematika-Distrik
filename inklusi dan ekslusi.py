from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Data jumlah mahasiswa
A = 175
B = 225
C = 200
AB = 50
AC = 60
BC = 70
ABC = 30

# Menghitung jumlah mahasiswa yang mengambil minimal satu mata kuliah
jumlah_minimal_satu = A + B + C - AB - AC - BC + ABC
print("Jumlah mahasiswa yang mengambil minimal satu mata kuliah:", jumlah_minimal_satu)

# Diagram Venn
# Hitung elemen masing-masing bagian
only_A = A - AB - AC + ABC
only_B = B - AB - BC + ABC
only_C = C - AC - BC + ABC
only_AB = AB - ABC
only_AC = AC - ABC
only_BC = BC - ABC
only_ABC = ABC

# Buat diagram
venn3(subsets=(only_A, only_B, only_AB, only_C, only_AC, only_BC, only_ABC),
      set_labels=('Matematika Diskrit (A)', 'Arsitektur Komputer (B)', 'Aljabar Linier (C)'))

plt.title("Diagram Venn Mata Kuliah")
plt.show()4-;;
