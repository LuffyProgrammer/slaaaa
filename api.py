from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
	return '''
{
    "status": "200"
    "message": "NÃO TEM NADA AQUI PORRA!"
}'''

@app.route('/teste')
def api1():
	return '''
{
    "status": "200"
    "message": "Clarisse, me chupa kkkkkkkkkkh"
}'''


def run():
	app.run(host='ssserverapi.herokuapp.com')

def keep_alive():

	t = Thread(target=run)
	t.start()
