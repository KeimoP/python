#Keimo Koolist
#04.10.2024
#H01

print('"Cabernet Sauvignon" või \'Cabernet Sauvignon\'?')

print('''
  @..@
 (----)
( \__/ )
^^ "" ^^
''')

#int täisarv 123
#str sõne "text"
#float komaarv 1.23

try:
    pikkus = int(input("Sisesta ruudu külje pikkus: "))
    vastus = pikkus * pikkus
    vastus = pikkus ** 2 #astendamine
    print("Ruudu pindala on",vastus,"cm2")
except:
    print("Kirjutasid valesti")
    
