import serial

valor1 = 10
valor2 = 20

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM4'
ser.open()
dados = '{:02d}{:02d}\n'.format(valor1,valor2)
ser.write(bytes(dados, 'utf-8'))
line = ser.readline() 
print(line)
ser.close()