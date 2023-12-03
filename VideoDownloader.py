
import yt_dlp

print("--------------------------------------------------")
print("-------- MARJAN POZEN! MI SMO PRPRAVLJEN! --------")
print("--------------------------------------------------")
print()

# pridobimo link do posnetka
ytLink = input("Vnesi link do posnetka:")

if ytLink == "":
    input("Nisi vnesel linka... ponovno zazeni in vnesi link!")
    exit()

# nastavimo pot do mape, kamor se bo posnetek shranil
yt_opts = {
    'paths': {"home":"${USERPROFILE}/Downloads/"}
}

# by default je izbran posnetek z najboljso locljivostjo vendar ne vec kot 720p
yt_dlp.YoutubeDL(yt_opts).download([ytLink])

print()
print("------------------- ZAKLUCENO -------------------")
print()
print("----- POSNETEK JE PRENESEN V MAPO DOWNLOADS -----")
print()
print("-------------------------------------------------")