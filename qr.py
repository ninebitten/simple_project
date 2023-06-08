import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=WgTMeICssXY")
img.save("youtube.png")