from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
    "Contact": "7249117985",
        "Name": "Raju",
        "done": false,
        "id":1
    },
    {
        "contact" : "7249116890"
        "Name": "Rahul",
        "done": false,
        "id":2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['title'],
        'contact': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)