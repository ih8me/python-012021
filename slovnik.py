# #
# # item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
# # item["price"] = 929
# # print("Cena polozky je " + str(item["price"]) + ".")
# # print("Cena polozky je ", item['price'], ".", sep = "")
# # print(f"Cena polozky je {item['price']}.")
# # item["weight"] = 0.5
# # if "weight" in item:
# #     print(f"Hmotnost je {item['weight']} kg.")
# # else:
# #     print("Hmotnost neni zadana.")
#
# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
# sausages.pop("Adam")
# print(len(sausages))

# vysvedceni = {"cesky jazyk": 2, "matematika": 1, "dejepis": 3}
# print(vysvedceni)
#
# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# sales["Noc, která mě zabila"] = 0
# sales["Vrah zavolá v deset"] = 5781
# print(sales)
#
# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
#
# numberOfTicket = int(input('Jake je cislo vaseho listku?'))
# if numberOfTicket in tombola:
#     print(f"Vyhral(a) jste {tombola[numberOfTicket]}.")
#     tombola.pop(numberOfTicket)
# else:
#     print("Bohužel nevyhráváš nic.")
# print(tombola)

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
#
# person = input('Jake je vase jmeno? ')
# if person in passwords:
#     heslo = input("Jake je vase heslo? ")
#     if heslo == passwords[person]:
#         print ("Smíš vstoupit.")

# baliky = {
#     "B541X": True,
#     "B547X": False,
#     "B251X": False,
#     "B501X": True,
#     "B947X": False,
# }
#
# code = input('Jaky je kod vaseho baliku? ')
# if code in baliky:
#     if baliky[code]:
#         print("Balík byl předán kurýrovi.")
#     else:
#         print("Balík zatím nebyl předán kurýrovi.")
# else:
#     print("Balík neexistuje.")

# sklad = {
#   "1N4148": 250,
#   "BAV21": 54,
#   "KC147": 147,
#   "2N7002": 97,
#   "BC547C": 10
# }
#
# code = input('Jaky je kod soucastky? ')
# if code in sklad:
#   mnozstvi = int(input('Kolik kusu si chcete koupit? '))
#   if sklad[code] < mnozstvi:
#     print("fLze prodat pouze {sklad[vstup]} kusů.")
#     sklad.pop(vstup)
#   else:
#     print("Poptávku lze uspokojit v plné výši.")
#     sklad[code] -= mnozstvi
# else:
#     print("Soucastka neni skladem.")

# volnePokoje = {
#   9: ["Amadeus", "Goya", "Vlasy"],
#   10: ["Forman", "Goya"],
#   11: [],
#   12: ["Amadeus", "Vlasy"]
# }
#
#  hodina = int(input("Zadej hodinu: "))
#  print(f"Pocet volnych zasedacek je {len(volnePokoje[hodina])}")
#
# morseCode = {
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
#     ".": ".-.-.-",
#     ",": "--..--",
#     "?": "..--..",
#     "!": "-.-.--",
#     "-": "-....-",
#     "/": "-..-.",
#     "@": ".--.-.",
#     "(": "-.--.",
#     ")": "-.--.-"
# }
#
# vstup = input("Zadej vstup: ")
# for i in vstup:
#   print(morseCode[i], end=" ")
#
# prodeje2019 = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
#
# prodeje2020 = {
#     "Zkus mě chytit": 3157,
#     "Vrah zavolá v deset": 3541,
#     "Vražda podle knihy": 2510,
#     "Past": 2364,
#     "Zločinný steh": 5412,
# }
#
# kniha = input("Zadej nazev knihy: ")
# soucet = 0
# if kniha in prodeje2019:
#   soucet = soucet + prodeje2019[kniha]
# print(f"Bylo prodano {soucet} kusu knih.")


# knihy = [
#   {"title": "Zkus mě chytit", "sold": 4165, "price": 347},
#   {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299},
#   {"title": "Zločinný steh", "sold": 2565, "price": 369}
# ]
#
# soucet=0
# for polozka in knihy:
#     soucet = soucet + polozka["prodano"] * polozka["cena"]
# print(soucet)


books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

pocet_stran = 0
pocet_knih = 0
for item in books:
    pocet_stran += item["pages"]
    if item ['rating']> 7:
        pocet_knih += 1
print(f"Gustav precetl {pocet_stran} pocet stran.")
print(f"Gustav precetl {pocet_knih} knihy s dobrym ratingem.")
