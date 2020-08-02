## Bot Quijote de la Mancha 

A bot that (almost) answers like don quijote.

### How to use

1. Install all the necesary libraries.

2. Start the server with ./start.sh

3. Call the api using

´´´
import requests

start_text = "Entonces Don Quijote "

r = requests.post(
    "http://127.0.0.1:5000/api/predict/",
    data= start_text).json()

print(r['text']))
´´´