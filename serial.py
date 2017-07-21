import serial //PySeial kütüphanesini ekleyin

ser = serial.Serial('COM3', baudrate = 9600, timeout =1) //COM BAUDRATE ayarla, bağlantı kur.

while 1:
    arduinoData = ser.readline()        //Gelen verileri al
    print(arduinoData) //Verileri yazdır
