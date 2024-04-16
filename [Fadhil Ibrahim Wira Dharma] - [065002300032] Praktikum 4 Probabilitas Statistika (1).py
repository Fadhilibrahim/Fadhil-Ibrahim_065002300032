#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

# Fungsi untuk menghitung kombinasi n choose k
def n_choose_k(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# Fungsi untuk menghitung probabilitas P(X=k) dalam distribusi binomial
def binomial_probability(n, k, p):
    return n_choose_k(n, k) * (p**k) * ((1-p)**(n-k))

# Parameter distribusi binomial
n = 10   # jumlah percobaan
p = 0.5  # probabilitas keberhasilan dalam satu percobaan (perbaikan: angka harus antara 0 dan 1)
k = 3    # jumlah keberhasilan yang ingin dihitung probabilitasnya

# Menghitung probabilitas
hasil_probabilitas = binomial_probability(n, k, p)
print("Probabilitas dari distribusi binomial:", hasil_probabilitas)


# In[6]:


from scipy.stats import binom

n = 10
p = 0.5
k = 3

prob_binomial = binom.pmf(k, n, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[11]:


import math

# Fungsi untuk menghitung probabilitas P(X=k) dalam distribusi Poisson
def poisson_probability(lambd, k):
    return (lambd**k) * math.exp(-lambd) / math.factorial(k)

lambd = 3  # Rata-rata jumlah peristiwa dalam interval waktu atau ruang tertentu
k = 2      # Jumlah peristiwa yang ingin dihitung probabilitasnya

prob_poisson = poisson_probability(lambd, k)
print("Probabilitas P(X=k) untuk distribusi Poisson:", prob_poisson)


# In[13]:


from scipy.stats import poisson

lambd = 3
k = 2

prob_poisson = poisson.pmf(k, lambd)
print("Probabilitas P(X=k) untuk distribusi poisson:", prob_poisson)


# In[16]:


from scipy import stats
X = stats.binom(15, 0.1)
print(X.pmf(3))    


# In[19]:


from scipy.stats import binom

# Parameter distribusi binomial
n = 15  # jumlah barang yang dibeli
p = 0.1  # probabilitas barang rusak

# Mencetak probabilitas kumulatif bahwa jumlah barang rusak kurang dari atau sama dengan 2
print(X.cdf(2)) #


# In[20]:


from scipy.stats import binom

n = 15
p = 0.1
print(X.pmf(6)+X.pmf(7))


# In[21]:


from scipy.stats import poisson
Y = stats.poisson(5)
print(Y.pmf(4))


# In[23]:


from scipy import stats
X = stats.binom(20, 0.7)
pmf_15 = X.pmf(15)
print(pmf_15)


# In[24]:


from scipy import stats
Y = stats.poisson(2)
print(Y.pmf(3))    #(P(Y=3))


# In[2]:


from scipy.stats import binom

n = 15
p = 0.3
k = 5

prob_binomial = binom.pmf(k, n, p)
print("Probabilitas tepat 5 dari 15 perangkat yang mengalami kegagalan:", prob_binomial)


# In[ ]:




