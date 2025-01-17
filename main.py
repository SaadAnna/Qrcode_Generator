import qrcode 
img = qrcode.make("https://x.com/CodewFront_end")
img.save("qrcode.png")