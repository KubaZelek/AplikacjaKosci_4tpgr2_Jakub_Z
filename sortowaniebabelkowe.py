#BABELKOWE


#
#
#

# tablica = []
# def wprowadz_dane():
#     for i in range(1,6):
#         liczba = int(input(f"Podaj liczbę {i} "))
#         tablica.append(liczba)
# def sort_bobel():
    
#     for i in range(len(tablica)):
#         for j in range(0, len(tablica)-i-1):
#             if tablica[j]<tablica[j+1]:
#                 tablica[j+1], tablica[j] = tablica[j], tablica[j+1]
# def wyprowadz_dane():
#     print(tablica)                    
# # sortowanie_babelkowe()
# wprowadz_dane()
# wyprowadz_dane()
# sort_bobel()
# wyprowadz_dane()


### 




# tablica = []
# tablica_uporzadkowana = []
# def wprowadz_dane():
#     for i in range(1,6):
#         liczba = int(input(f"Podaj liczbę {i} "))
#         tablica.append(liczba)
# def sort_wstaw():
#     for i in range(len(tablica)):
#         element = tablica[i]
#         j = i - 1
#         while j >= 0 and tablica_uporzadkowana[j] > element:
#             j -= 1
#         tablica_uporzadkowana.insert(j + 1, element)
#         print(tablica_uporzadkowana)


# def wyprowadz_dane():
#     print(f"Tablica 1: {tablica}")
#     print(f"Tablica 2:{tablica_uporzadkowana}")                    
# sortowanie_babelkowe()
# tablica = []

# def wprowadz_dane():
#     for i in range(1, 6):
#         liczba = int(input(f"Podaj liczbę {i}: "))
#         tablica.append(liczba)

# def sort_wstaw(tab):
#     if len(tab) <= 1:  
#         return tab

#     mid = len(tab) // 2
#     L = tab[:mid]
#     R = tab[mid:]

#     L = sort_wstaw(L) 
#     R = sort_wstaw(R)  

#     i,j = 0, 0 
#     result = []

#     length_L = len(L)
#     length_R = len(R)

#     while i < length_L and j < length_R:
#         if L[i] < R[j]:
#             result.append(L[i])
#             i += 1
#         else:
#             result.append(R[j])
#             j += 1

#     while i < length_L:
#         result.append(L[i])
#         i += 1

#     while j < length_R:
#         result.append(R[j])
#         j += 1

#     return result

# def wyprowadz_dane():
#     print(f"Tablica: {tablica}")


# wprowadz_dane()
# wyprowadz_dane()
# tablica = sort_wstaw(tablica)
# wyprowadz_dane()



tablica = []

def wprowadz_dane():
    for i in range(1, 6):
        liczba = int(input(f"Podaj liczbę {i}: "))
        tablica.append(liczba)

def sort_wstaw(tab, start, end):
    pivot = tab[end]
    low = start
    high = end - 1
    
    while True:
        while low <= high and tab[low] <= pivot:
            low += 1
        while low <= high and tab[high] >= pivot:
            high -= 1
        if low <= high:
            tab[low], tab[high] = tab[high], tab[low]
        else:
            break
    
    tab[end], tab[low] = tab[low], tab[end]
    return low

def sortowanko(tab, start, end):
    if start < end:
        pivot = sort_wstaw(tab, start, end)
        sortowanko(tab, start, pivot - 1)
        sortowanko(tab, pivot + 1, end)
        print(tab)

def wyprowadz_dane():
    print(f"Tablica: {tablica}")

wprowadz_dane()
wyprowadz_dane()
sortowanko(tablica, 0, len(tablica) - 1)
wyprowadz_dane()
