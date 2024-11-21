from flask import Flask, render_template, request, jsonify
from pyproj import Geod

app = Flask(__name__)
geod = Geod(ellps='WGS84')

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
