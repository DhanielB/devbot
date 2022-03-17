from flask import Flask
from threading import Thread
import urllib.request

app = Flask('')

@app.route('/')
def home():
  return "I'm alive"
def run():
  app.run(host='0.0.0.0',port=8080)
  try:
    page = urllib.request.urlopen('https://DevApp.dhanielb.repl.co')
    print(page.read())
  except:
    print("Cannot request!")
  

def keep_alive():
  t = Thread(target=run)
  t.start()