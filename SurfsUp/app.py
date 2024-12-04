# Import the dependencies.
from flask import Flask, jsonify
from datetime import datetime, timedelta

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the most recent date in the dataset
    one_year_ago = datetime.now() - timedelta(days=365)

    # Query the precipitation data for the last year
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Create a dictionary from the results
    precip_data = {date: prcp for date, prcp in results}

    # Return the JSON representation of the dictionary
    return jsonify(precip_data)
