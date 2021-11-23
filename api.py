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
	app.run(host='https://ssserverapi.herokuapp.com/', port=random.randint(2000, 9000))

def keep_alive():

	t = Thread(target=run)
	t.start()
