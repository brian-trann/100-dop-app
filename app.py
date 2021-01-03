from flask import Flask, render_template, redirect
from gpiozero import LEDBoard
from time import sleep

app = Flask(__name__)
leds= LEDBoard(18,23,24,25,12,16,20,21,pwm=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on')
def on():
    leds.on()
    return redirect('/')

@app.route('/off')
def off():
    leds.off()
    return redirect('/')

@app.route('/test')
def test():
    for led in leds[::2]:
        led.on()
    return redirect('/')

@app.route('/test99')
def test99():
    num = 99
    leds.off()
    for i in get_led_indexes(num):
        leds[i].blink()
    return redirect('/')

def get_led_indexes(num):
    '''This function takes in a number, converts to binary. 
    If the bit is ON, led, at that index turns on'''
    arr = []
    for i in range(0,8):
        if num & (1 << i):
            arr.append(i)
    return arr

