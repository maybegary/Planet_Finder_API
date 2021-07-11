from types import MethodDescriptorType
from typing import ClassVar
from flask import Flask, url_for, request, jsonify, g
from flask.templating import render_template
from typing import Text
from numpy import integer
from skyfield import data
from skyfield.api import load
from skyfield.planetarylib import PlanetTopos
from skyfield.positionlib import Astrometric

planets = load('de421.bsp')

ts = load.timescale()
t = ts.now()

planets = load('de421.bsp')

earth = planets['earth']
local_planets = [planets['mercury'], planets['venus'],planets['mars'],planets['jupiter barycenter'],planets['saturn barycenter'],planets['uranus barycenter'],planets['neptune barycenter'],planets['pluto barycenter']]

app = Flask(__name__)

@app.route("/API", methods=['GET'])
def planet_rad_get():
    data2 = []
    for i in range(len(local_planets)):
        astrometric = earth.at(t).observe(local_planets[i])
        ra,dec,distance = astrometric.radec()
        data = (str(ra),str(dec),str(distance))
        data2.append(data)
        
    return jsonify(data2)


@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)