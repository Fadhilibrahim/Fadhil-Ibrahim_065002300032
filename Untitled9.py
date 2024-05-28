#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import chi2_contingency

# Data kontingensi
# Baris: Pendapatan (A, B, C)
# Kolom: Kualitas bahan makanan (Tinggi, Sedang, Rendah)
observed = np.array([
    [14,  6,  9],  # A (Pendapatan Tinggi)
    [10, 16, 10],  # B (Pendapatan Sedang)
    [ 2, 13, 20]   # C (Pendapatan Rendah)
])

# Lakukan uji chi-squared
chi2, p, dof, expected = chi2_contingency(observed)

# Tampilkan hasil
print("Chi-squared test")
print(f"X-squared = {chi2:.3f}")
print(f"df = {dof}")
print(f"p-value = {p:.6f}")

# Tampilkan frekuensi yang diharapkan
print("\nObserved Frequencies:")
print(observed)

print("\nExpected Frequencies:")
print(np.round(expected, 2))

# Tentukan apakah ada hubungan antara pendapatan dan kualitas bahan makanan
alpha = 0.05
if p > alpha:
    print("\nTidak ada hubungan yang signifikan antara pendapatan dan kualitas bahan makanan (gagal menolak H0)")
else:
    print("\nAda hubungan yang signifikan antara pendapatan dan kualitas bahan makanan (menolak H0)")


# In[2]:


import numpy as np
from scipy import stats

# Data sampel nilai dari 15 mahasiswa
data = [12, 25, 45, 67, 43, 33, 24, 45, 34, 11, 8, 34, 67, 99, 22]

# Urutkan data secara ascending
data_sorted = np.sort(data)

# Hitung mean dan standar deviasi
mean = np.mean(data_sorted)
std = np.std(data_sorted, ddof=1)

# Lakukan uji Kolmogorov-Smirnov
stat, p_value = stats.kstest(data_sorted, 'norm', args=(mean, std))

# Tampilkan hasil
print("Kolmogorov-Smirnov test")
print(f"Statistik uji: {stat:.3f}")
print(f"p-value: {p_value:.6f}")

# Bandingkan dengan nilai kritis D tabel
D_critical = 0.338  # dari soal untuk n=15 dan alpha=0.05

# Tentukan apakah data berdistribusi normal atau tidak
if stat > D_critical:
    print("Tolak H0: Populasi data tidak berdistribusi normal")
else:
    print("Gagal menolak H0: Populasi data berdistribusi normal")


# In[ ]:




