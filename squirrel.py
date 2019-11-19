from flask import Flask
import random
from threading import Thread

app = Flask('')

url = ["https://github.com/rexjohannes/rex-api/raw/squirrel/the-squirrel-566745__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/the-squirrel-4571711__340.jpg",
"https://github.com/rexjohannes/rex-api/raw/squirrel/the-squirrel-2708860__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/the-squirrel-2680397__340.jpg",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-803621__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-659264__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-619968__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-56928__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-493790__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4616708__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4615620__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4604576__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4519518__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4477611__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4473622_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4467299__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4466632__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4466617__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4463626__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4337341__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4333647__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4318302__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4310069__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4232129__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-4026286__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-3715663__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-3632880__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-3032060__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2787409__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2671234__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2478517__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2410583__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2187369__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2187362__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2116188__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2115581__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2115579__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-2040481__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-1228613__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-1228610__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-1075440__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/squirrel-1000386__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animals-3971502__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animals-3525923__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-world-4400807__340.jpg",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-605329__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-316528__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-2092791__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-2047108__340.webp",
"https://github.com/rexjohannes/rex-api/raw/squirrel/animal-1125102__340.webp"]

@app.route('/')
def home():
    return random.choice(url)

def run():
  app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()
