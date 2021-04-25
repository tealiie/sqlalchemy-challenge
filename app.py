import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"To view all percipitation:<br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        f"To view all stations:<br/>"
        f"/api/v1.0/stations<br><br/>"
        f"To view all tobs for most active station in the past year:<br/>"
        f"/api/v1.0/tobs<br><br/>"
        f"To view min, max and avg for tobs from a start date: YYYY-MM-DD <br/>"
        f"/api/v1.0/<start><br><br/>"
        f"To view min, max and avg for tobs between a start date and end date: YYYY-MM-DD / YYYY-MM-DD <br>"
        f"/api/v1.0/<start>/<end>"
    )


# Convert the query results to a dictionary using date as the key and prcp as the value
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.prcp).all()
    
    session.close()
    
    all_percip = []
    for date, prcp in results:
        percip_dict = {}
        percip_dict["date"] = date
        percip_dict["prcp"] = prcp
        all_percip.append(percip_dict)
            
    return jsonify(all_percip)
    

# Return a JSON list of stations from the dataset.    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    results = session.query(Station.station, Station.name).all()
  
    session.close()
    
    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)
        
    return jsonify(all_stations)


# Query the dates and temperature observations of the most active station for the last year of data
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date > '2016-08-23').\
        filter(Measurement.date < '2017-08-23').all()
        
    session.close()
        
    active_station_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        active_station_tobs.append(tobs_dict)
     
    return jsonify(active_station_tobs)
        

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start_date>")
def start_date_tobs(start_date):
    session = Session(engine)
           
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
       filter(Measurement.date > start_date).all()
           
    session.close()
    
    # start_date use format YYYY-MM-DD
           
    start_tobs = []
    for min, max, avg in results:
        start_dict = {}
        start_dict["min"] = min
        start_dict["max"] = max
        start_dict["avg"] = avg
        start_tobs.append(start_dict)
                         
    return jsonify(start_tobs)


# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date_tobs(start_date, end_date):
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
       filter(Measurement.date > start_date).\
       filter(Measurement.date < end_date).all()
    
    session.close()
    
    # start_date use format YYYY-MM-DD
    # end_date use format YYYY-MM-DD

    start_end_tobs = []
    for min, max, avg in results:
        start_end_dict = {}
        start_end_dict["min"] = min
        start_end_dict["max"] = max
        start_end_dict["avg"] = avg
        start_end_tobs.append(start_end_dict)
                         
    return jsonify(start_end_tobs)


if __name__ == '__main__':
    app.run(debug=True)
