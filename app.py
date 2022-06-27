from flask import Flask, render_template, request
import serial

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/enviar", methods=['POST'])
def enviar():
    valor1 = int(request.form['valor1'])
    valor2 = int(request.form['valor2'])
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM4'
    ser.open()
    dados = '{:02d}{:02d}\n'.format(valor1,valor2)
    ser.write(bytes(dados, 'utf-8'))
    line = ser.readline() 
    print(line)
    ser.close()
    return render_template('index.html')