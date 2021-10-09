import pandas as pd
import streamlit as st
import pickle as pkl
from sklearn.cluster import KMeans
from PIL import Image

st.title('Klasterisasi Zona COVID-19')

img = Image.open('cover_covid_indonesia.png')
st.image(img, width = 685)

st.write("""
### Model ini dikembangkan oleh tim **The Chosen** dengan menggunakan **Python** dan **Streamlit**
""")

st.write('##### Anggota:')
st.write('##### - Adam Maurizio Winata')
st.write('##### - Alvin Bimo Ramadhani')
st.write('##### - Muhammad Axel Syahputra')
st.write('##### - Yohanes Manasye Triangga')

st.write(" [Link Dashboard](https://bit.ly/DashboardTSDN)")

display = ('Pilih Jumlah Klaster','Klaster 2 Zona', 'Klaster 3 Zona', 'Klaster 4 Zona')

value = st.selectbox("Masukkan jumlah klaster", display)

if value == "Pilih Jumlah Klaster":
    st.write(' ')

elif value == "Klaster 2 Zona":
    model = pkl.load(open('kluster2zona_covid19.sav', 'rb'))
    suspek = st.number_input(label = 'Masukkan Jumlah Kasus Suspek : ', min_value=0, step=1000, key='1')
    positif = st.number_input(label = 'Masukkan Jumlah Kasus Positif : ', min_value=0, step=1000, key='2')
    dirawat = st.number_input(label = 'Masukkan Jumlah Kasus Dirawat : ', min_value=0, step=1000, key='3')
    sembuh = st.number_input(label = 'Masukkan Jumlah Kasus Sembuh : ', min_value=0, step=1000, key='4')

    dt = pd.DataFrame()
    dt['Suspek'] = [suspek]
    dt['Positif'] = [positif]
    dt['Dirawat'] = [dirawat]
    dt['Sembuh'] = [sembuh]

    y_pred = model.predict(dt)

    st.write('Tabel Situasi COVID-19')
    st.write(dt)

    if int(y_pred) == 0:
        st.write('Daerah Anda masuk ke kategori Zona Hijau')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 1 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial 75 persen kerja dari kantor atau work from office (WFO) jika sudah divaksin ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 75 persen dan buka hingga pukul 21.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup bisa buka dengan kapasitas 75 persen ')
        st.write('- Kegiatan belajar mengajar 50 persen daring dan 50 persen tatap muka ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 50 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 1:
        st.write('Daerah Anda masuk ke kategori Zona Merah')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 3 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial kerja dari rumah atau work from home (WFH) ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 15.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 25 persen dan tutup pukul 17.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 25 persen dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup hanya melayani take away/delivery ')
        st.write('- Kegiatan belajar mengajar 100 persen daring ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 25 persen dan protokol kesehatan ketat.')

elif value == "Klaster 3 Zona":
    model = pkl.load(open('kluster3zona_covid19.sav', 'rb'))
    suspek = st.number_input(label = 'Masukkan Jumlah Kasus Suspek : ', min_value=0, step=1000, key='5')
    positif = st.number_input(label = 'Masukkan Jumlah Kasus Positif : ', min_value=0, step=1000, key='6')
    dirawat = st.number_input(label = 'Masukkan Jumlah Kasus Dirawat : ', min_value=0, step=1000, key='7')
    sembuh = st.number_input(label = 'Masukkan Jumlah Kasus Sembuh : ', min_value=0, step=1000, key='8')

    dt = pd.DataFrame()
    dt['Suspek'] = [suspek]
    dt['Positif'] = [positif]
    dt['Dirawat'] = [dirawat]
    dt['Sembuh'] = [sembuh]

    y_pred = model.predict(dt)

    st.write('Tabel Situasi COVID-19')
    st.write(dt)

    if int(y_pred) == 0:
        st.write('Daerah Anda masuk ke kategori Zona Hijau')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 1 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial 75 persen kerja dari kantor atau work from office (WFO) jika sudah divaksin ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 75 persen dan buka hingga pukul 21.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup bisa buka dengan kapasitas 75 persen ')
        st.write('- Kegiatan belajar mengajar 50 persen daring dan 50 persen tatap muka ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 50 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 1:
        st.write('Daerah Anda masuk ke kategori Zona Kuning')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 2 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial 50 persen work from office (WFO) jika sudah divaksin ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 50 persen dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup bisa buka dengan kapasitas 50 persen ')
        st.write('- Kegiatan belajar mengajar 50 persen daring dan 50 persen tatap muka ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 50 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 2:
        st.write('Daerah Anda masuk ke kategori Zona Merah')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 3 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial kerja dari rumah atau work from home (WFH) ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 15.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 25 persen dan tutup pukul 17.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 25 persen dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup hanya melayani take away/delivery ')
        st.write('- Kegiatan belajar mengajar 100 persen daring ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 25 persen dan protokol kesehatan ketat.')

elif value == "Klaster 4 Zona":
    model = pkl.load(open('kluster3zona_covid19.sav', 'rb'))
    suspek = st.number_input(label = 'Masukkan Jumlah Kasus Suspek : ', min_value=0, step=1000, key='9')
    positif = st.number_input(label = 'Masukkan Jumlah Kasus Positif : ', min_value=0, step=1000, key='10')
    dirawat = st.number_input(label = 'Masukkan Jumlah Kasus Dirawat : ', min_value=0, step=1000, key='11')
    sembuh = st.number_input(label = 'Masukkan Jumlah Kasus Sembuh : ', min_value=0,step=1000, key='12')

    dt = pd.DataFrame()
    dt['Suspek'] = [suspek]
    dt['Positif'] = [positif]
    dt['Dirawat'] = [dirawat]
    dt['Sembuh'] = [sembuh]

    y_pred = model.predict(dt)

    st.write('Tabel Situasi COVID-19')
    st.write(dt)

    if int(y_pred) == 0:
        st.write('Daerah Anda masuk ke kategori Zona Hijau')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 1 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial 75 persen kerja dari kantor atau work from office (WFO) jika sudah divaksin ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen ')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 75 persen dan buka hingga pukul 21.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup bisa buka dengan kapasitas 75 persen ')
        st.write('- Kegiatan belajar mengajar 50 persen daring dan 50 persen tatap muka ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 50 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 1:
        st.write('Daerah Anda masuk ke kategori Zona Merah')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 3 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial kerja dari rumah atau work from home (WFH) ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 15.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 25 persen dan tutup pukul 17.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 25 persen dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup hanya melayani take away/delivery ')
        st.write('- Kegiatan belajar mengajar 100 persen daring ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 25 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 2:
        st.write('Daerah Anda masuk ke kategori Zona Kuning')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 2 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial 50 persen work from office (WFO) jika sudah divaksin ')
        st.write('- Pekerjaan esensial beroperasi 100 persen dengan dibagi menjadi 2 shift dengan protokol kesehatan ketat ')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 75 persen dan tutup pukul 21.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00 ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas 50 persen dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup bisa buka dengan kapasitas 50 persen ')
        st.write('- Kegiatan belajar mengajar 50 persen daring dan 50 persen tatap muka ')
        st.write('- Tempat ibadah dibuka dengan kapasitas 50 persen dan protokol kesehatan ketat.')
    elif int(y_pred) == 3:
        st.write('Daerah Anda masuk ke kategori Zona Hitam')
        st.write('Usaha yang perlu dilakukan adalah PPKM level 4 dengan rincian sebagai berikut:')
        st.write('- Pekerjaan non-esensial kerja dari rumah atau work from home (WFH) ')
        st.write('- Pekerjaan esensial beroperasi 50 persen dengan dibagi menjadi 1 shift dan 100 persen WFO untuk untuk kritikal dengan protokol kesehatan ketat')
        st.write('- Toko atau pasar kebutuhan sehari-hari bisa buka dengan kapasitas 50 persen dan tutup pukul 20.00')
        st.write('- Pasar rakyat selain kebutuhan sehari-hari bisa buka dengan kapasitas 25 persen dan tutup pukul 15.00')
        st.write('- Pusat perbelanjaan seperti mall dan plaza tutup kecuali apotik dan toko obat ')
        st.write('- Pedagang kaki lima (PKL), barbershop dan sejenisnya bisa buka sampai pukul 20.00 ')
        st.write('- Warung makan, PKL, lapak jajanan di ruang terbuka boleh beroperasi dengan kapasitas maksimal 3 orang n dan buka hingga pukul 20.00. Sementara pengunjung yang makan di tempat diberi batas waktu maksimal 30 menit. ')
        st.write('- Restoran di ruang tertutup hanya melayani take away/delivery ')
        st.write('- Kegiatan belajar mengajar 100 persen daring ')
        st.write('- Tempat ibadah dilarang ada kegiatan berjamaah.')
