#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.stats import norm

mean = 184
std_dev = 5

height = 189
prob_less_than_189 = norm.cdf(mean, std_dev, height)

print("probabilitas kurang dari 189:", prob_less_than_189)


# In[3]:


from scipy.stats import norm

mean = 184
std_dev = 5

prob_less_174 = norm.cdf(174, mean, std_dev)
prob_less_199 = norm.cdf(199, mean, std_dev)

prob_between_174_and_199 = prob_less_199 - prob_less_174

print("Probabilitas tinggi antara 174cm dan 199cm:", prob_between_174_and_199)


# In[5]:


from scipy.stats import norm

mean = 173
std_dev = 34
berat = 120

berat_kurang_dari_120 = norm.cdf(berat, mean, std_dev)

print("Peluang apel yang berkualitas 'not good': {:.4f}".format(berat_kurang_dari_120))


# In[7]:


arrival_rate = 1/10
service_rate = 1/8

L = arrival_rate / (service_rate - arrival_rate)
W = L / arrival_rate

print("Rata-rata jumlah pelanggan dalam sistem (L): {:.2f}".format(L))
print("Rata-rata waktu setiap pelanggan berada dalam sistem (W): {:.2f}".format(W))


# In[14]:


from scipy.stats import expon

mean_service_time = 7

prob_between_3_and_5 = expon.cdf(5, scale=mean_service_time) - expon.cdf(3, scale=mean_service_time)

print("peluang seseorang dilayani antara 3 sampai 5 menit: {:.7f}".format(prob_between_3_and_5))


# In[15]:


from scipy.stats import poisson

mean_arrival_rate = 5

prob_more_than_6_arrival = 1 - poisson.cdf(6, mean_arrival_rate*2)

print("peluang bahwa lebih dari 6 pelanggan akan tiba dalam periode 2 menit berikutnya: {:.7f}".format(prob_more_than_6_arrival))


# In[1]:


from scipy.stats import norm

mean = 184
std_dev = 5
berat = 120

berat_kurang_dari_120 = norm.cdf(berat, mean, std_dev)

print("Peluang apel yang berkualitas 'not good': {:.4f}".format(berat_kurang_dari_120))


# In[3]:


from scipy.stats import norm

mean = 184
std_dev = 5

prob_more_than = 1 - 0.1685

height = norm.ppf(prob_more_than, mean, std_dev)

print("Tinggi sedemikian rupa sehingga 16,85% pemain basket lebih tinggi dari {:.2f}cm".format(height))


# In[4]:


from scipy.stats import binom

n = 8
p = 0.06

prob_not_good_2_or_less = binom.cdf(2,n,p)

print("Probabilitas kurang dari atau sama dengan 2 apel berkualitas 'not good': {:.7f}".format(prob_not_good_2_or_less))


# In[6]:


arrival_rate_new = 1/16
service_rate = 1/8

L_new = arrival_rate_new / (service_rate - arrival_rate_new)
W_new = L_new / arrival_rate_new 

print("Rata-rata jumlah pelanggan dalam sistem (L) setelah perubahan: {:.2f}".format(L_new))
print("Rata-rata waktu setiap pelanggan berada dalam sistem (W) setelah perubahan: {:.2f}".format(W_new))


# In[7]:


from scipy.stats import expon

mean_waktu = 7
prob_lebih_dari_8_menit = 1 - expon.cdf(8, scale=mean_waktu)

print("Peluang  seseorang mendapatkan pelayanan lebih dari 8 menit:{:.7f}".format(prob_lebih_dari_8_menit))


# In[8]:


from scipy.stats import poisson

mean_arrival_rate = 5
prob_4_arrivals = poisson.pmf(4, mu=mean_arrival_rate)

print("Peluang bahwa dalam 1 menit berikutnya terdapat tepat 4 pelanggan yang akan datang: {:.7f}".format(prob_4_arrivals))


# In[ ]:




