import streamlit as st
import joblib 
tf_random_forest = joblib.load('./rf_classification_model.pkl')
    

#mebuat footer

def main():
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pergi ke", ("Beranda", "Pohon 1", "Pohon 2", "Pohon 3", "Pohon 4", "Pohon 5","Credit"))

    # Konten berdasarkan navigasi
    if page == "Beranda":      
    # Judul Dashboard
        st.title('Input Preferensi Pengguna')

        # Pilihan untuk Favorite Color
        favorite_color = st.selectbox('Pilih Warna Favorit:', ['Cool', 'Neutral', 'Warm'])

        # Pilihan untuk Favorite Music Genre
        favorite_genre = st.selectbox('Pilih Genre Musik Favorit:', ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic', 'R&B and soul'])

        # Pilihan untuk Favorite Beverage
        favorite_beverage = st.selectbox('Pilih Minuman Favorit:', ['Vodka', 'Wine', 'Whiskey', 'Doesn\'t drink', 'Beer', 'Other'])

        # Pilihan untuk Favorite Soft Drink
        favorite_soft_drink = st.selectbox('Pilih Minuman Ringan Favorit:', ['7UP/Sprite', 'Coca Cola/Pepsi', 'Fanta', 'Other'])


        # Tombol untuk submit
        submitted = st.button('Submit')

        st.subheader('Hasil Prediksi:')
        # Tampilkan hasil jika tombol submit ditekan
        if submitted:
            st.write('Preferensi Pengguna:')
            st.write(f'- Warna Favorit: {favorite_color}')
            st.write(f'- Genre Musik Favorit: {favorite_genre}')
            st.write(f'- Minuman Favorit: {favorite_beverage}')
            st.write(f'- Minuman Ringan Favorit: {favorite_soft_drink}')

            # Konversi pilihan warna favorit ke nilai numerik
            if favorite_color == 'Cool':
                favorite_color = 0.0
            elif favorite_color == 'Neutral':
                favorite_color = 0.5
            elif favorite_color == 'Warm':
                favorite_color = 1.0
            else:
                favorite_color = 0.0

            # Konversi pilihan genre musik favorit ke nilai numerik
            if favorite_genre == 'Rock':
                favorite_genre = 1.0
            elif favorite_genre == 'Hip hop':
                favorite_genre = 0.3333333333333333
            elif favorite_genre == 'Folk/Traditional':
                favorite_genre = 0.16666666666666666
            elif favorite_genre == 'Jazz/Blues':
                favorite_genre = 0.5
            elif favorite_genre == 'Pop':
                favorite_genre = 0.6666666666666666
            elif favorite_genre == 'Electronic':
                favorite_genre = 0.0
            elif favorite_genre == 'R&B and soul':
                favorite_genre = 0.8333333333333333
            else:
                favorite_genre = 0.0

            # Konversi pilihan minuman favorit ke nilai numerik
            if favorite_beverage == 'Vodka':
                favorite_beverage =  0.6000000000000001
            elif favorite_beverage == 'Wine':
                favorite_beverage = 1.0
            elif favorite_beverage == 'Whiskey':
                favorite_beverage = 0.8 
            elif favorite_beverage == "Doesn't drink":
                favorite_beverage = 0.2 
            elif favorite_beverage == 'Beer':
                favorite_beverage = 0.0 
            elif favorite_beverage == 'Other':
                favorite_beverage = 0.4
            else:
                favorite_beverage = 0.0

            # Konversi pilihan minuman ringan favorit ke nilai numerik
            if favorite_soft_drink == '7UP/Sprite':
                favorite_soft_drink = 0.0
            elif favorite_soft_drink == 'Coca Cola/Pepsi':
                favorite_soft_drink = 0.3333333333333333
            elif favorite_soft_drink == 'Fanta':
                favorite_soft_drink = 0.6666666666666666
            elif favorite_soft_drink == 'Other':
                favorite_soft_drink = 1.0
            else:
                favorite_soft_drink = 0.0

            # Prediksi preferensi pengguna menggunakan model random forest
            prediction = tf_random_forest.predict([[favorite_color, favorite_genre, favorite_beverage, favorite_soft_drink]])
            accuracy = tf_random_forest.score([[favorite_color, favorite_genre, favorite_beverage, favorite_soft_drink]], prediction)
            gender = ""
            if prediction[0] == 1:
                gender = "Laki-laki"
            else:
                gender = "Perempuan"
            st.write(f'Prediksi Gender: {gender}')
            st.write(f'Accuracy: {accuracy}')
    elif page == "Pohon 1":
        st.header("Pohon 1")
        st.image("./Tree/RandomForestTree_0.png.png", caption="struktur pohon dari algoritma decision tree", use_column_width=True)
    elif page == "Pohon 2":
        st.header("Pohon  2")
        st.image("./Tree/RandomForestTree_1.png.png", caption="struktur pohon dari algoritma decision tree", use_column_width=True)
    elif page == "Pohon 3":
        st.header("Pohon  3")
        st.image("./Tree/RandomForestTree_2.png.png", caption="struktur pohon dari algoritma decision tree", use_column_width=True)
    elif page == "Pohon 4":
        st.header("Pohon  4")
        st.image("./Tree/RandomForestTree_3.png.png", caption="struktur pohon dari algoritma decision tree", use_column_width=True)
    elif page == "Pohon 5":
        st.header("Pohon  5")
        st.image("./Tree/RandomForestTree_4.png.png", caption="struktur pohon dari algoritma decision tree", use_column_width=True)
    elif page == "Credit":
        st.header("Anggota Kelompok")
        st.write("1. Muhammad Alvi Kirana Zulfan Nazal (23051204339)")
        st.write("2. Mochamad Fajar Krisdianto (23051204327)")
        st.write("3. Nofi Ayu Wulandari (23051204326)")
        st.write("4. Khoerunnisa Utami (23051204340)")

    st.markdown("""
    ---
    © 2024 Aplikasi Kami | Dibuat dengan ❤️ oleh Kami \n
    Support system by Allah SWT
    """)

if __name__ == "__main__":
    main()

