# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engin = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engin)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engin)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes - API Dynamic Route 
#################################################

@app.route("/")  """List all available api routes."""
def welcome():
    return(
        f"Welcome to Hawaii Weather API"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start><end>"
    )

@app.route(/api/v1.0/<start>)
def start(start):
    canonicalized = start.replace("")
    for date in stat_summary:
        search_date = date['start'].replace("")
        if search date == canonicalized:
            return jsonify(sta_summary)
    return jasonify ({"error":f"start date {start} not fount"}), 404

@app.route(/api/v1.0/<star><end>)
def start_end():
    canonicalized = start_end.replace("","")
    for date, date in temperature:
        start_date = date['start']


