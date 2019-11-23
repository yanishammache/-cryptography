crypto_deb_decalage=input("Enter a key : ")

if crypto_deb_decalage < chr(48) or crypto_deb_decalage > chr(57):
	crypto_fin_decalage = ord(crypto_deb_decalage)
else:
	crypto_fin_decalage = int(crypto_deb_decalage)

crypto_valeur=input("Enter what you want : ")


message_secret = crypto_valeur
message_code =""
message_decode =""

for lettre in message_secret :
    nb_lettre = ord(lettre)
    nb_lettre_code = nb_lettre + crypto_fin_decalage
    lettre_code = chr(nb_lettre_code)
    message_code += lettre_code
print(message_code)

for lettre_code in message_code :
    nb_lettre_code = ord(lettre_code)
    nb_lettre = nb_lettre_code - crypto_fin_decalage
    lettre = chr(nb_lettre)
    message_decode += lettre
print(message_decode)