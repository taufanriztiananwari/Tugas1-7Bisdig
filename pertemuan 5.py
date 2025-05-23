# -*- coding: utf-8 -*-
"""taufan Riztian Anwari pertemuan 5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19WTohFw6_Er6LKHxbB_-R6Ol3OBS1qnC

# New Section

# pertemuan 5
"""

# Contoh penggunaan
A = [[4, 2, 1], [5, 5, 6]]
B = [[7, 9, 9], [2, 8, 3]]

# contoh matrix penjumlahan

def matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


print("Penjumlahan Matriks:")
print(matrix(A, B))

# contoh matrix pengurangan
def matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

# Contoh penggunaan
print("Pengurangan Matriks:")
print(matrix(A, B))

#contoh matrix perkalian
def matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result


print("Perkalian Matriks:")
print(matrix(A, B))

# Contoh penggunaan
array = [5, 3, 8, 1, 4]

def find_max_min(arr):
    max_value = max(arr)
    min_value = min(arr)
    return max_value, min_value

max_value, min_value = find_max_min(array)
print("Nilai Maksimum:", max_value)
print("Nilai Minimum:", min_value)

def text_processor():
    text = input("Masukkan teks: ")

    # Statistik
    word_count = len(text.split())
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print("Jumlah Kata:", word_count)
    print("Jumlah Karakter:", char_count)
    print("Jumlah Kalimat:", sentence_count)

    # Pencarian Kata
    search_word = input("Masukkan kata yang ingin dicari: ")
    occurrences = text.lower().count(search_word.lower())
    print(f"Kata '{search_word}' ditemukan sebanyak {occurrences} kali.")

    # Penggantian Teks
    old_word = input("Masukkan kata yang ingin diganti: ")
    new_word = input("Masukkan kata pengganti: ")
    new_text = text.replace(old_word, new_word)
    print("Teks setelah penggantian:\n", new_text)

    # Format Teks
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title Case:", text.title())

# Contoh penggunaan
text_processor()
