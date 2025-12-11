from flask import Flask, request, jsonify
from cinema import AdvancedStatistics

app = Flask(_name_)
cinema = AdvancedStatistics()

@app.post("/add")
def add_movie():
    data = request.json
    cinema.add_movie(
        data["title"], 
        data["genre"], 
        int(data["views"]),
        float(data["rating"])
    )
    return jsonify({"status": "OK"})

@app.get("/report")
def report():
    cinema.analyze()
    return jsonify(cinema._results)

if _name_ == "_main_":
    app.run(debug=True)
