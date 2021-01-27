import time
import itertools

def read_code(filename):
    cd_file = open(filename, 'r')
    wordlist = cd_file.readlines()
    mod_wl = []
    hasil = wordlist[len(wordlist)-1]
    for i in range(len(wordlist)):
        mod_wl.append(wordlist[i].strip().replace("\n", "").replace("-","").replace("+", ""))

    kamus = []
    for teks in mod_wl:
        for kata in teks:
            if kata not in kamus:
                kamus.append(kata)

    mod_wl.pop()
    mod_wl.pop()
    return kamus, mod_wl, hasil

def str_to_int(word, word_dict):
    tot = 0
    f = 1
    for huruf in reversed(word):
        tot += f*word_dict[huruf]
        f *= 10
    return tot

def solvecryp(filename):
    count = 0
    kamus, wordlist, result = read_code(filename)
    solusi = []
    
    angka = range(10)
    for perm in itertools.permutations(angka, len(kamus)):
        kms2 = dict(zip(kamus, perm))

        if sum(str_to_int(kata, kms2) for kata in wordlist) == str_to_int(result, kms2):
            if kms2[result[0]] != 0:
                solusi = kms2
                count += 1
                break
        
        count += 1

    if len(solusi) != 0:
        return count, solusi, result, wordlist
    else:
        print("Tidak ditemukan solusi")

def main_prog(file_name):
    t1_start = time.process_time()
    
    count, solusi, result, wordlist = solvecryp(file_name)
    for word in wordlist:
        print()
        print(" "*(len(result)-len(word)), end="")
        print(word, end="")
    print("+")
    print("-"*(len(result)+1))
    print(result)

    for word in wordlist:
        print()
        print(" "*(len(result)-len(word)), end="")
        for letter in word:
            print(solusi[letter], end="")
    print("+")
    print("-"*(len(result)+1))
    for letter in result:
        print(solusi[letter], end="")

    print()
    print()
    print("Jumlah Percobaan : " + str(count))
    t1_stop = time.process_time() 
    print("Waktu program berjalan : " + str(t1_stop - t1_start) + " s")

#--------------------------------------------------------------
#----------------------- MAIN PROGRAM -------------------------
exit = 0
while exit == 0:
    file_name = input("Masukkan nama file : ")
    try :
        main_prog("../test/" + str(file_name))
    except :
        print("File tidak ditemukan")

    print()
    print("Ingin mencoba puzzle lain? (Y/N)")
    xy = input()
    
    if (xy == "N") or (xy == "n"):
        exit = 1

