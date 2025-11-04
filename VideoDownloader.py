
import yt_dlp
import os

print("--------------------------------------------------")
print("-------- MARJAN POZEN! MI SMO PRPRAVLJEN! --------")
print("--------------------------------------------------")
print()

# pridobimo link do posnetka
ytLink = input("Vnesi link do posnetka:")

if ytLink == "":
    input("Nisi vnesel linka... ponovno zazeni in vnesi link!")
    exit()

# nastavimo pot do ffmpeg.exe
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_PATH = os.path.join(BASE_DIR, "ffmpeg", "bin", "ffmpeg.exe")

# nastavimo pot do mape, kamor se bo posnetek shranil
yt_opts = {
    'paths': {"home":"${USERPROFILE}/Desktop/Kosarka/Prenosi/"},  
    'ffmpeg_location': FFMPEG_PATH,
    # 1) raje HLS (m3u8) in/ali MP4 do 720p
    "format": (
        "b[protocol^=m3u8][height<=720]/"   # HLS (kot tvoj format 301, ki dela)
        "b[ext=mp4][height<=720]/"          # MP4 do 720p
        "b[ext=mp4]/"                       # katerikoli MP4
        "best"                              # kot fallback (če res nič drugega ne gre)
    ),
    'merge_output_format': 'mp4', # opcijsko – remux v mp4, če je mogoče
    # 1) raje HLS (m3u8) in/ali MP4 do 720p
    "format": (
        "b[protocol^=m3u8][height<=720]/"   # HLS (kot tvoj format 301, ki dela)
        "b[ext=mp4][height<=720]/"          # MP4 do 720p
        "b[ext=mp4]/"                       # katerikoli MP4
        "best"                              # kot fallback (če res nič drugega ne gre)
     )
}

# by default je izbran posnetek z najboljso locljivostjo vendar ne vec kot 720p
yt_dlp.YoutubeDL(yt_opts).download([ytLink])

print()
print("------------------- ZAKLUCENO -------------------")
print()
print("----- POSNETEK JE PRENESEN V MAPO DOWNLOADS -----")
print()
print("-------------------------------------------------")