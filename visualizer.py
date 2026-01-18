import streamlit as st
import random
import time

# Arayüz Yapılandırması
st.set_page_config(page_title="Algoritma Görselleştirici", layout= "wide")
st.title("Bubble Sort Görselleştirici")

# Yan menüde ayarları yapalım
with st.sidebar:
    st.header("Ayarlar")
    liste_boyutu = st.slider("Liste Boyutu", 10, 100, 30)
    hiz = st.slider("Hız (Saniye)", 0.01, 0.5, 0.1)

# Veri Oluşturucu
# Slider'dan gelen 'liste_boyutu' değiştiğinde listeyi otomatik yenile
# Veri Oluşturucu Kısmını Şöyle Güncelle:
if 'liste' not in st.session_state or len(st.session_state['liste']) != liste_boyutu:
    st.session_state['liste'] = random.sample(range(1, 101), liste_boyutu)

# Grafiği yerleştireceğimiz boş alan
grafik_alani = st.empty()
grafik_alani.bar_chart(st.session_state['liste'])

# Algoritma ve Görselleştirme
def bubble_sort(arr):
    n = len(arr)
    baslangic_zamani= time.time() # Zamanlayıcıyı başlat

    for i in range(n):
        for j in range(0, n - i -1):
            # iki elemanı karşılaştırıyor
            if arr[j] > arr[j+1]:
                #swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Görselleştirme Anı
                # Her swap işleminden sonra grafiği güncelle
                grafik_alani.bar_chart(arr)
                if hiz > 0:
                    time.sleep(hiz)

    bitis_zamani = time.time() # Zamanlayıcıyı durdur
    return  round(bitis_zamani - baslangic_zamani , 2)


# Kontrol Paneli
c1, c2 = st.columns(2)
with c1:
    if st.button("Sıralamayı başlat ve Ölç!"):
        gecen_sure = bubble_sort(st.session_state.liste)

        #Sonuç Ekranı
        st.divider()
        st.balloons() # Kutlama Efekti

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Toplam Süre", f"{gecen_sure} sn")
        with col2:
            st.metric("Algoritma", "Bubble Sort")
        with col3:
            st.metric("Karmaşıklık", "$O(n^2)$")
        st.success(f"İşlem başarıyla tamamlandı! {liste_boyutu} eleman {gecen_sure} saniyede sıralandı.")
with c2:
    if st.button("Listeyi Karıştır"):
        st.session_state.liste = random.sample(range(1,101), liste_boyutu)
        st.rerun()
