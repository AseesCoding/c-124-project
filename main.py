from flask import Flask, jsonify

app = Flask(__name__)
print(app)

contact = [
    {
        'id':1,
        'name':u'Ramesh',
        'contact':9988776655,
        'done': False
    },
    {
        'id':2,
        'name':u'Ram',
        'contact':9988776650,
        'done': False
    }
]

@app.route("/")
def a():
    return "Put '/add-data' in URL"

@app.route("/add-data")

def gettingdata():
    return jsonify({"data":contact})

if(__name__=="__main__"):
    app.run(debug=True)