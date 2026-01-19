import streamlit as st
import random
import time

# Arayüz Yapılandırması
st.set_page_config(page_title="Algoritma Görselleştirici", layout="wide")
st.title("Algoritma Görselleştirici")

# --- YAN MENÜ ---
with st.sidebar:
    st.header("Algoritma Seçimi")
    algoritma_secimi = st.selectbox("Algoritma Seçin", ["Insertion Sort","Selection Sort", "Bubble Sort","Heap Sort", "Merge Sort","Quick Sort" ])

    st.header("Ayarlar")
    liste_boyutu = st.slider("Liste Boyutu", 10, 100, 30)
    hiz = st.slider("Hız (Saniye)", 0.0, 0.5, 0.05)

# --- VERİ YÖNETİMİ ---
if 'liste' not in st.session_state or len(st.session_state['liste']) != liste_boyutu:
    st.session_state['liste'] = random.sample(range(1, 101), liste_boyutu)

if 'sayac' not in st.session_state:
    st.session_state.sayac = 0

# Grafiği yerleştireceğimiz boş alan
grafik_alani = st.empty()
grafik_alani.bar_chart(st.session_state['liste'])


# --- ALGORİTMALAR ---

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Her swap işleminden sonra grafiği güncelle
                st.session_state.sayac += 1
                grafik_alani.bar_chart(arr)
                if hiz > 0:
                    time.sleep(hiz)

# 2. Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            st.session_state.sayac += 1
            grafik_alani.bar_chart(arr)
            if hiz > 0:
                time.sleep(hiz)
        arr[j + 1] = key
        st.session_state.sayac += 1
        grafik_alani.bar_chart(arr)
        if hiz > 0:
            time.sleep(hiz)

# 3. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        pos= i
        for j in range(i+1,n):
            st.session_state.sayac += 1
            grafik_alani.bar_chart(arr)
            if hiz > 0:
                time.sleep(hiz)
            if arr[j] < arr[pos]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]
        st.session_state.sayac += 1
        grafik_alani.bar_chart(arr)
        if hiz > 0:
            time.sleep(hiz)

# 4. Quick Sort (Partition ve Recursive Fonksiyon)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            st.session_state.sayac += 1
            grafik_alani.bar_chart(arr)
            if hiz > 0:
                time.sleep(hiz)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    st.session_state.sayac += 1
    grafik_alani.bar_chart(arr)
    if hiz > 0:
        time.sleep(hiz)
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i  # Kökü en büyük kabul et
    left = 2 * i + 1
    right = 2 * i + 2
    # Karşılaştırmayı görselleştir (Adalet dokunuşu)
    if hiz > 0:
        grafik_alani.bar_chart(arr)
        time.sleep(hiz / 5)
    # Sol çocuk kökten büyük mü?
    if left < n and arr[i] < arr[left]:
        largest = left
    # Sağ çocuk şu ana kadarki en büyükten büyük mü?
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Eğer en büyük kök değilse yer değiştir
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Yer değiştirmeyi (Swap) görselleştir
        grafik_alani.bar_chart(arr)
        if hiz > 0:
            time.sleep(hiz)
        # Alt ağacı tekrar heapify yap
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # 1. Max-Heap oluştur (Build heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 2. Elemanları tek tek heap'ten çıkar
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # En büyüğü sona taşı
        grafik_alani.bar_chart(arr)
        if hiz > 0:
            time.sleep(hiz)
        # Kalanlarla tekrar heap yapısını kur
        heapify(arr, i, 0)


def merge(arr, l, m, r):
    # Geçici diziler oluşturulur
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = 0  # Sol alt dizinin indeksi
    j = 0  # Sağ alt dizinin indeksi
    k = l  # Ana dizinin indeksi
    while i < n1 and j < n2:
        # ADALET DOKUNUŞU: Karşılaştırmayı görselleştir
        if hiz > 0:
            grafik_alani.bar_chart(arr)
            time.sleep(hiz / 5)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        # Eleman ana diziye yerleşirken görselleştir
        grafik_alani.bar_chart(arr)
        if hiz > 0: time.sleep(hiz)
        k += 1
    # Kalan elemanlar varsa eklenir
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        grafik_alani.bar_chart(arr)
        if hiz > 0: time.sleep(hiz)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        grafik_alani.bar_chart(arr)
        if hiz > 0: time.sleep(hiz)


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        # Sol ve sağ yarıları rekürsif olarak parçala
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        # Parçaları birleştir
        merge(arr, l, m, r)


# --- KONTROL PANELİ ---
c1, c2 = st.columns(2)

with c1:
    if st.button("Sıralamayı Başlat ve Ölç!"):
        st.session_state.sayac = 0
        baslangic_zamani = time.time()

        # Seçilen algoritmaya göre çalıştır
        if algoritma_secimi == "Insertion Sort":
            insertion_sort(st.session_state['liste'])
            kompleksite = "$O(n^2)$"
        elif algoritma_secimi == "Selection Sort":
            selection_sort(st.session_state['liste'])
            kompleksite = "$O(n^2)$"
        elif algoritma_secimi == "Bubble Sort":
            bubble_sort(st.session_state['liste'])
            kompleksite = "$O(n^2)$"
        elif algoritma_secimi == "Quick Sort":
            quick_sort(st.session_state['liste'], 0, len(st.session_state['liste']) - 1)
            kompleksite = "$O(n \log n)$"
        elif algoritma_secimi == "Heap Sort":
            heap_sort(st.session_state['liste'])
            kompleksite = "$O(n \log n)$"
        elif algoritma_secimi == "Merge Sort":
            merge_sort(st.session_state['liste'], 0, len(st.session_state['liste']) - 1)
            kompleksite = "$O(n \log n)$"

        gecen_sure = round(time.time() - baslangic_zamani, 2)

        # Sonuç Ekranı
        st.divider()
        st.balloons()

        col1, col2, col3, col4= st.columns(4)
        with col1:
            st.metric("Toplam Süre", f"{gecen_sure} sn")
        with col2:
            st.metric("Algoritma", algoritma_secimi)
        with col3:
            st.metric("Karmaşıklık", kompleksite)
        with col4:
            st.metric("UI Güncelleme Sayısı", st.session_state.sayac)
        st.success(f"İşlem başarıyla tamamlandı! {liste_boyutu} eleman {gecen_sure} saniyede sıralandı.")


with c2:
    if st.button("Listeyi Karıştır"):
        st.session_state['liste'] = random.sample(range(1, 101), liste_boyutu)
        st.rerun()