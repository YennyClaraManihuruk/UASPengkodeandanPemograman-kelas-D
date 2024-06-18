import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Membaca dataset
data = pd.read_csv('data_penjualan.csv')

# Pembersihan Data

# Mengubah tipe data Tanggal menjadi datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Mengatasi nilai yang hilang
data = data.dropna()

# Menghapus duplikasi
data = data.drop_duplicates()

# Memastikan tipe data yang tepat
data['Jumlah'] = data['Jumlah'].astype(int)
data['Pendapatan'] = data['Pendapatan'].astype(float)

# Visualisasi Data

# Pie Chart - Persentase jumlah buku terjual per jenis buku
jumlah_per_buku = data.groupby('Nama_Buku')['Jumlah'].sum()
plt.figure(figsize=(8, 8))
plt.pie(jumlah_per_buku, labels=jumlah_per_buku.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Persentase Jumlah Buku Terjual per Jenis Buku')
plt.show()

# Scatter Plot - Jumlah buku terjual vs. Pendapatan
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Jumlah', y='Pendapatan', hue='Nama_Buku', palette='viridis', s=100, data=data)
plt.title('Scatter Plot Jumlah Buku Terjual vs. Pendapatan')
plt.xlabel('Jumlah Buku Terjual')
plt.ylabel('Pendapatan')
plt.legend(title='Nama Buku')
plt.show()

# Line Plot - Trend penjualan buku dari waktu ke waktu
plt.figure(figsize=(12, 6))
for buku in data['Nama_Buku'].unique():
    buku_data = data[data['Nama_Buku'] == buku]
    plt.plot(buku_data['Tanggal'], buku_data['Jumlah'], marker='o', linestyle='-', label=buku)
plt.title('Trend Penjualan Buku')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Buku Terjual')
plt.legend(title='Nama Buku')
plt.grid(True)
plt.show()

# Histogram - Distribusi jumlah buku terjual
plt.figure(figsize=(10, 6))
sns.histplot(data['Jumlah'], bins=20, kde=True, color='skyblue')
plt.title('Distribusi Jumlah Buku Terjual')
plt.xlabel('Jumlah Buku')
plt.ylabel('Frekuensi')
plt.show()

# Box Plot - Distribusi pendapatan per jenis buku
plt.figure(figsize=(10, 6))
sns.boxplot(x='Nama_Buku', y='Pendapatan', palette='Set2', data=data)
plt.title('Distribusi Pendapatan per Jenis Buku')
plt.xlabel('Nama Buku')
plt.ylabel('Pendapatan')
plt.show()

# Bar Plot - Total penjualan per jenis buku
plt.figure(figsize=(10, 6))
sns.barplot(x='Nama_Buku', y='Jumlah', palette='Set1', data=data.groupby('Nama_Buku')['Jumlah'].sum().reset_index())
plt.title('Total Penjualan per Jenis Buku')
plt.xlabel('Nama Buku')
plt.ylabel('Jumlah Terjual')
plt.show()

# 3D Scatter Plot - Jumlah buku terjual vs. Pendapatan vs. Tanggal
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(data['Tanggal'].map(pd.Timestamp.toordinal), data['Jumlah'], data['Pendapatan'], c=data['Jumlah'], cmap='coolwarm', s=100)
ax.set_title('3D Scatter Plot Jumlah Buku Terjual vs. Pendapatan vs. Tanggal')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Buku Terjual')
ax.set_zlabel('Pendapatan')
plt.colorbar(scatter, ax=ax, label='Jumlah Buku Terjual')
plt.show()
