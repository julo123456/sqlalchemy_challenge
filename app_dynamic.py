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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes - API Dynamic Route 
#################################################

@app.route("/")  #"""List all available api routes."""
def welcome():
    return(
        f"Welcome to Hawaii Weather API"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start><end>"
    )

@app.route("/api/v1.0/<start>")
def start(start):
    canonicalized = start.replace("")
    sel_station = [
               func.max(measurement.tobs),
               func.min(measurement.tobs),
               func.avg(measurement.tobs)]
    sta_summary = session.query(*sel_station).filter(measurement.date >= start).all()

    session.close()
    return jsonify ([sta_summary])

@app.route("/api/v1.0/<start><end>")
def start_end(start,end):
    sel_station = [
            func.max(measurement.tobs),
            func.min(measurement.tobs),
            func.avg(measurement.tobs)]
    sta_summary = session.query(*sel_station).filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    session.close()
    return jsonify ([sta_summary])


