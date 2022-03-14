def show_menu():
    print('Silahkan pilih menu yang bisa aku berikan')
    print('1. Menghitung dengan kalkulator')
    print('2. Menemani curhatmu')
    print('3. Keluar')

#Pengantar
print('Hai, aku AIs, asisten virtual pertamamu')
print('Siapa namamu?')

nama = input('Masukkan nama:')

print("\nSalam kenal {}".format(nama))
print('Apa ada yang bisa aku bantu?')

#Munculkan menu awal
while True:
    print(' ')
    show_menu()
    
    menu_awal = input('\nPilih hanya angka saja ya:')
    
    if menu_awal == '1':
        operasi = input('Silahkan pilih menu= 1:Penjumlahan, 2:Pengurangan, 3:Perkalian, 4:Pembagian, 5:Keluar')
        if operasi == '1':
            x = int(input('Masukkan angka ke-1:'))
            y = int(input('Masukkan angka ke-2'))
            print('Nilai {} + {}'.format(x,y),'=',x+y)
            print('==========================')
        elif operasi == '2':
            x = int(input('Masukkan angka ke-1:'))
            y = int(input('Masukkan angka ke-2'))
            print('Nilai {} - {}'.format(x,y),'=',x-y)
            print('==========================')
        elif operasi == '3':
            x = int(input('Masukkan angka ke-1:'))
            y = int(input('Masukkan angka ke-2'))
            print('Nilai {} x {}'.format(x,y),'=',x*y)
            print('==========================')
        elif operasi == '4':
            x = int(input('Masukkan angka ke-1:'))
            y = int(input('Masukkan angka ke-2'))
            print('Nilai {} : {}'.format(x,y),'=',x/y)
            print('==========================')
        elif operasi == '5':
            print('\nOke, terima kasih telah menggunakan kalkulator ini')
            print('==========================')
        else:
            print('\nMaaf, pilihan menu angka tidak ada')
            print('==========================')

        
    elif menu_awal == '2':
        input('Coba ceritakan curhatmu:')
        while True:
            
            Cerita= input('Coba ceritakan lebih banyak lagi:')
            
            if 'bodoh' in Cerita or 'gagal' in Cerita or 'kalah' in Cerita or 'jelek' in Cerita:
                print('Kenapa kamu berpikir seperti itu?')
            elif 'kecewa' in Cerita or 'sedih' in Cerita or 'putus asa' in Cerita:
                print('Sudah berapa lama kamu merasa seperti itu?')
            elif 'senang' in Cerita or 'berhasil' in Cerita or 'menang' in Cerita or 'hadiah' in Cerita:
                print('Itu sangan menarik!')
            else:
                print('\nOke, tetap semangat ya!', ':)')
                print("=====================")
                break
    
    elif menu_awal == '3':
        print("\nOke, sampai jumpa")
        print("=====================")
        break
    else:
        print("\nMaaf, aku belum paham yang kamu mau")
        print("=====================")