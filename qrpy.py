import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 4 variables diferentes



#convertir cada variable a entero

  
"""
crear la funcnion operacion 
esta funcion devolera el resultado de:
w elevado a la x, dividido para y elevado a la z
"""


#convertir este resutado en string


#mostrar el resultado en el qr
resultado = operacion(w,x,y,z)
print(resultado)
img = qrcode.make(str(resultado))
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")
