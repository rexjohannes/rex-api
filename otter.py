from flask import Flask
import random
from threading import Thread

app = Flask('')

url = ["https://github.com/rexjohannes/rex-api/raw/otter/animal-1994495_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/animal-1994496_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/animal-845228_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/big-otter-mill-4539940_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/clawed-otter-2146072_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/clawed-otter-406968_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/nature-3547073_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1042063_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1145555_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1438378_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1438381_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1522378_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1717204_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-1982429_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2487214_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2500234_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2539518_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2549855_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2549856_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-2678776_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-327585_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-327587_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634132_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634133_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634152_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634157_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634158_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3634162_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-365370_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-365371_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-365372_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3738269_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3801698_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-3818817_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-4367998_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-4444711_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-4455006_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-4455022_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/zoo-4331430_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-4563763_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-468868_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-498046_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-7473_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-779457_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-779458_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-838021_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-840049_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/otter-90025_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/otters-2434082_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/relaxed-1143733_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/sea-otter-1432794_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/sea-otter-3194446_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/sea-otter-3194450_960_720.webp",
"https://github.com/rexjohannes/rex-api/raw/otter/sea-otter-3194453_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/sea-otter-3314894_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/snow-3183034_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/sun-1828512_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/swim-69500_960_720.jpg",
"https://github.com/rexjohannes/rex-api/raw/otter/two-otters-342174_960_720.webp"]

@app.route('/')
def home():
    return random.choice(url)

def run():
  app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()
