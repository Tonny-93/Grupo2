import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 4 variables diferentes
print "w=2"
print "x=4"
print "y=2"
print "z=6"

#convertir cada variable a entero
print "w^x/y^z"
  
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
