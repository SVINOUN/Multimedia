file = open('./images/volcan.bmp','rb')
# Sugerencia: cambié el nombre de salida a volcan_lavanda.bmp
fileo = open('./images/volcan_lavanda.bmp','wb') 
metadata = file.read(54)
fileo.write(metadata)

# Tonos lavanda en formato BGR (Azul, Verde, Rojo)
# Van desde morado oscuro (lavanda1) hasta un lavanda casi blanco (lavanda16)
lavanda1  = [0x2B, 0x10, 0x20] 
lavanda2  = [0x3F, 0x1B, 0x2F]
lavanda3  = [0x52, 0x26, 0x3E]
lavanda4  = [0x66, 0x31, 0x4C]
lavanda5  = [0x79, 0x3C, 0x5B]
lavanda6  = [0x8D, 0x47, 0x6A]
lavanda7  = [0xA1, 0x52, 0x79]
lavanda8  = [0xB4, 0x5D, 0x87]
lavanda9  = [0xC8, 0x68, 0x96]
lavanda10 = [0xD2, 0x7E, 0xA5]
lavanda11 = [0xDC, 0x94, 0xB4]
lavanda12 = [0xE6, 0xAA, 0xC3]
lavanda13 = [0xF0, 0xC0, 0xD2]
lavanda14 = [0xF5, 0xD6, 0xE1]
lavanda15 = [0xFA, 0xE1, 0xEB]
lavanda16 = [0xFF, 0xF0, 0xF5] 

file.seek(54,0)
no_pix = 0
limite = (pow(2 ,24)-1)/16

while(True):
    pixel_data = file.read(3)
    if(len(pixel_data) > 0):
        valor_int = int.from_bytes(pixel_data, byteorder='little')
        
        if valor_int < limite:
            color_elegido = lavanda1
        elif valor_int < limite * 2:
            color_elegido = lavanda2
        elif valor_int < limite * 3:
            color_elegido = lavanda3
        elif valor_int < limite * 4:
            color_elegido = lavanda4
        elif valor_int < limite * 5:
            color_elegido = lavanda5
        elif valor_int < limite * 6:
            color_elegido = lavanda6
        elif valor_int < limite * 7:
            color_elegido = lavanda7
        elif valor_int < limite * 8:
            color_elegido = lavanda8
        elif valor_int < limite * 9:
            color_elegido = lavanda9
        elif valor_int < limite * 10:
            color_elegido = lavanda10
        elif valor_int < limite * 11:
            color_elegido = lavanda11
        elif valor_int < limite * 12:
            color_elegido = lavanda12
        elif valor_int < limite * 13:
            color_elegido = lavanda13
        elif valor_int < limite * 14:
            color_elegido = lavanda14
        elif valor_int < limite * 15:
            color_elegido = lavanda15
        else:
            color_elegido = lavanda16
            
        fileo.write(bytes(color_elegido))
        no_pix += 1
    else:
        break

print('No Pixels: '+str(no_pix))
file.close()
fileo.close()