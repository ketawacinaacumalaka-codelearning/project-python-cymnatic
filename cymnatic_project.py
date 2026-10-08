import os 
import random

def main():
    daftar_kata = ["PYTHON", "KOMPUTER", "VARIABEL", "ALGORITMA", "DATABASE", "CYMNATIC", "CYBER", "INTEGER", "STRING", "BOOLEAN"]
    kata_rahasia = random.choice(daftar_kata)#variable list kata rahasia
    
    nyawa = 7 #variable nyawa nya
    tebakan_huruf = []#buat masukin huruf yang di tebak ke list
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']#gambar indikator gamenya
    
    print("====================================")
    print("Selamat datang di permainan Hangman!")
    print("====================================")


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')#biar abis jawab yg dia atas di bersihin
        print(HANGMANPICS[6 - nyawa])
        kata_tertebak = ""
        menang = True
        
        for huruf in kata_rahasia:
            if huruf in tebakan_huruf:
                kata_tertebak += huruf + " "
            else:
                kata_tertebak += "_ "
                menang = False

        print(f"\nKata: {kata_tertebak}")#fstring biar ke bawah katanya
        print(f"Nyawa tersisa: {nyawa}")
        
        if menang:
            print("Selamat! Kamu berhasil menebak katanya!")
            print("Kamu berhasil menyelamatkan Rusdi :)")
            input("\nTekan Enter untuk keluar...") # Menahan terminal biar gak langsung tutup
            break

        if nyawa <= 0:
            print(f"Kamu kalah! masa gitu aja gak bisa awokawok Kata rahasianya adalah {kata_rahasia}")#ngambil kata yg di pilih dari list

            # PERBAIKAN: Simpan hasil input ke variabel
            jawaban = input("Apakah kamu mau ke minigame untuk kesempatan ke dua? (ya/tidak): ")
            
            if jawaban.lower() == "ya": #Nested if
                print("\nSelamat datang di minigame! Kamu akan diberikan kesempatan untuk menebak kata rahasia lagi.")
                
                # PERBAIKAN: Gunakan print untuk soal, bukan input
                print("Soal: Apa nama bahasa pemrograman yang membuat game ini?")
                print("A. Java\nB. Python\nC. C++\nD. JavaScript")
                
                jawaban_kuis = input("Jawabanmu: ").upper()
                if jawaban_kuis == "B":
                    print("Jawaban kamu benar!\n")
                    main() # Main lagi
                else:
                    print("Jawaban kamu salah!")
                    input("\nTekan Enter untuk keluar...")
                    break#buat stop
            else:
                print("Terima kasih telah bermain! Sampai jumpa lagi.")
                input("\nTekan Enter untuk keluar...")
                break    #buat stop

        tebakan = input("Tebak 1 huruf: ").upper()

        if tebakan in tebakan_huruf:
            print("Huruf ini sudah kamu tebak! Coba huruf lain.")
        else:
            tebakan_huruf.append(tebakan)
            
            if tebakan not in kata_rahasia:
                nyawa -= 1
                print("Tebakan SALAH!")
            else:
                print("Tebakan BENAR!")

main()