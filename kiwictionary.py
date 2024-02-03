import random
print("Słowa w słowniku: CRINGE, LOL, ROFL, CREEPY, AGGRO, TREW")
meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "odpowiedź na żart",
            "CREEPY" : "straszny, złowieszczy",
            "AGGRO" : "stać się agresywnym/zły",
            "UWU" : "Nie pytaj, błagam.",
            "TREW" : "Prawda, tylko inaczej",
            "BTW" : "przy okazji"
            }


word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
 
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Nic nie znaleziono.")
