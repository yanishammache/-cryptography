crypto_deb_decalage=input("Enter a key : ")

if crypto_deb_decalage < chr(48) or crypto_deb_decalage > chr(57):
	crypto_fin_decalage = ord(crypto_deb_decalage)
else:
	crypto_fin_decalage = int(crypto_deb_decalage)

crypto_valeur=input("Enter what you want : ")


message_secret = crypto_valeur
message_code =""
message_decode =""

#########################
# on chiffre le message #
#########################

for lettre in message_secret :          # Pour chaque lettre du message
    nb_lettre = ord(lettre)             # On récupère le numéro Ascii de la lettre
    nb_lettre_code = nb_lettre + crypto_fin_decalage      # On y ajoute 3
    lettre_code = chr(nb_lettre_code)   # On reconverti en lettre
    message_code += lettre_code         # On ajoute la nouvelle lettre au message codé
print(message_code)


######################################################################
# Pour déchiffrer le message on fait la même chose mais en enlevant 3#
######################################################################

for lettre_code in message_code :        # Pour chaque lettre du message codé
    nb_lettre_code = ord(lettre_code)    # On récupère le numéro Ascii de la lettre codée
    nb_lettre = nb_lettre_code - crypto_fin_decalage       # On y enlève 3
    lettre = chr(nb_lettre)              # On reconverti en lettre
    message_decode += lettre             # On ajoute la nouvelle lettre au message decodé
print(message_decode)