from flask import render_template, Flask, request
import csv

app = Flask(__name__)


@app.route('/')
def home():
    db = [line for line in csv.DictReader(open("data.csv"))]

    dog_age = float(request.args.get('age', 0.0))
    dog_weight = int(request.args.get('weight', 0))

    filtered = []
    for i in db:
        print(i)
        if float(i['min_age']) > dog_age:
            continue
        if float(i['max_age']) < dog_age:
            continue
        if int(i['min_weight']) > dog_weight:
            continue
        if int(i['max_weight']) < dog_weight:
            continue
        print("added")
        filtered.append(i)


    return render_template('index.html', data=filtered, dog_age=dog_age, dog_weight=dog_weight)
