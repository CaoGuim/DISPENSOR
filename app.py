import requests
from flask import Flask, render_template, redirect
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://teste-7f365-default-rtdb.firebaseio.com/', None)
link = "https://teste-7f365-default-rtdb.firebaseio.com/"


@app.route('/')
def red():
    return redirect('/welcome')


@app.route('/welcome', methods=['GET'])
def welcome():
    requisition = requests.get(f'{link}/estado/.json')
    dicestado = requisition.json()

    requisition = requests.get(f'{link}/valor/.json')
    dicvalor = requisition.json()
    return render_template('index.html', dicvalor=dicvalor, dicestado=dicestado)

if __name__ == '__main__':
    app.run(debug=False)
