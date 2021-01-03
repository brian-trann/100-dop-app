from flask import Flask, render_template, redirect, flash
from gpiozero import LEDBoard
from helpers import get_led_indexes
from forms import LEDForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
leds= LEDBoard(18,23,24,25,12,16,20,21,pwm=True)


@app.route('/',methods=["GET","POST"])
def index():
    form=LEDForm()
    if form.validate_on_submit():
        day_led = form.day.data
        mode= form.mode.data
        return redirect(f'/leds/{day_led}/{mode}')
    else:
        return render_template('index.html',form=form)

@app.route('/leds/on')
def on():
    '''Turn on all 8 LEDs'''
    leds.on()
    flash("All LEDs On","success")
    return redirect('/')

@app.route('/leds/off')
def off():
    '''Turn off all 8 LEDs'''
    leds.off()
    flash("All LEDs Off", 'danger')
    return redirect('/')

@app.route('/leds/<int:led_id>/<mode>')
def led_day(led_id,mode):
    leds.off()
    for i in get_led_indexes(led_id):
        if mode =='normal':
            leds[i].on()
        elif mode =='blink':
            leds[i].blink()
        else:
            leds[i].pulse()
    flash(f"You're on day: {led_id}. Mode: {mode}","success")
    return redirect('/')
