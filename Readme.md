## Bot Quijote de la Mancha 

![Don quijote logo](./assets/don-quixote.png)

Icon made by [Free Pik](https://www.flaticon.com/authors/freepik) from [flaticon.com](https://www.flaticon.com/)

A bot that (almost) talks like Don Quijote de la Mancha.

### How to use

1. Install all the necesary libraries.

2. Start the server with `./start.sh`

3. Call the api using

```
import requests

start_text = "Entonces Don Quijote"

r = requests.post(
    "http://127.0.0.1:5000/api/predict/",
    data= start_text).json()

print(r['text']))

>>> Entonces Don quijote quien tenía la verdad, y el de la misma ventana, y la más de las cosas dada de su parte en sus propesidos.
```