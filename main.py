from pytube import YouTube

link = input("Videonun linkini buraya giriniz:")
directory = input("İndirilen videonun adının ne olmasını istersiniz? ")

try:
    yt = YouTube(link)
except:
    print("Videonuz bulunamadı. Linki kontrol ediniz.")
    exit()

mp4s = yt.streams.filter(file_extension="mp4")

for i, mp4 in enumerate(mp4s):
    print(i + 1, mp4)

n = int(input("Çözünürlüğü seçiniz:"))

print("İndiriliyor...")

mp4s[n - 1].download(directory)

print("İndirme Tamamlandı!")
