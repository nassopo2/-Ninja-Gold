from flask import Flask, render_template, request, session, redirect, flash
import random
from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key = "343566it7iy8ouiphljhghfdgetw465768y8oi"

@app.route('/')
def index():
    if (session.get('gold') is None):
        session['gold'] = 0
    if "activity" not in session:
        session['activity'] = []
    length = len(session['activity'])
    return render_template('index.html', activity = session['activity'], length = length)

@app.route('/process_money', methods = ['POST'])
def payout():

   building = request.form['building']
   currentactivity = ""
   if request.form['building'] == 'farm':
        coin = random.randrange(10,21)
        session['gold'] = session['gold'] + coin
        currentactivity = "Earned" + " " + str(coin) +" " + "golds on the farm!"
   elif request.form['building'] == 'cave':
        coin = random.randrange(5,11)
        session['gold'] = session['gold'] + coin
        currentactivity = "Earned" + " " + str(coin) +" " + "golds in the cave!"
   elif request.form['building'] == 'home':
        coin = random.randrange(2,6)
        session['gold'] = session['gold'] + coin
        currentactivity = "Earned" + " " + str(coin) +" " + "golds at home!"
   elif request.form['building'] == 'casino':
        coin =  random.randrange(-50,50)
        session['gold'] = session['gold'] + coin
        if coin > 0:
           currentactivity = "Earned" + " " + str(coin) +" " + "golds at the casino!"
        elif coin == 0:
           currentactivity = "Broke even at the casino!"
        else:
           currentactivity = "Lost" + " " + str(coin) +" " + "golds at the casino!"
   now = str(datetime.now())
   now = now[:19]
   currentactivity += " (" + now + ")"
   session['activity'].append(currentactivity)
   return redirect ('/')


@app.route('/reset')
def reset():
    session['gold']=0
    session['activity']=[]
    return redirect('/')


app.run(debug=True)
