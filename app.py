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
# Flask Routes - API Static Route
#################################################
@app.route("/")  """List all available api routes."""
def welcome():
    return(
        f"Welcome to the Hawaii Weather API"
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )


##### API Static Routes#####
### API route for precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():  
    # Create session (link) from Python to the DB
    session = Session(engin)

    # Query restuls from precipitation analysis
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date <= '2017-08-23').filter(measurement.date >= query_date).all()

    session.close()

    # Create a dictionary from the query restuls from precipitaiton analysis
    last_precipitation = [] 
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['precipitation'] = prcp
        last_precipitation.append(precipitation_dict)
    
    return jsonify(last_precipitation)  


### API route for stations
@app.route("/api/v1.0/stations")
def stations():
    # Create session (link) from Python to the DB
    session = Session(engin)

    # Query results from stations analysis to list all stations
    results = session.query(measurement.station).distinct().all()
    session.close()

    # List all the stations from query restuls from station analysis to list all stations
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)  

### API route for temperatures
@app.route("api/v1.0/tobs")
def tobs():
    # Create session (link) from Python to the DB
    session = Session(engin)

    # Query results for the most active station
    results = sta_summary
    active_station = list(np.ravel(results))

    session.close()
    return jsonify(active_station) 

def tobs():
    # Create session (link) from Python to the DB
    session = Session(engin)

    # Query restuls last year of temperature data from the most active station
    results = temperature
    temp_active_station = list(np.ravel(results))

    session.close()
    return jsonify(temp_active_station)

if __name__ == '__main__':
    app.run(debug=True)

