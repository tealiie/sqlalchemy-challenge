# Climate Analyssi of Honolulu, Hawaii

## Instructions
Use Python and SQLAlchemy to do climate analysis and data exploration of the climate database in Honolulu, Hawaii. 

## Climate Analysis and Exploration
The following analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib

### Precipitation Analysis
* Design a query to retrieve the last 12 months of precipitation data.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data.

![Screen Shot 2021-08-27 at 2 05 13 PM](https://user-images.githubusercontent.com/19372031/131070419-749ab06c-6d84-4ec2-b5b7-ba1dab87ba34.png)

### Station Analysis
* Design a query to calculate the total number of stations.
* Design a query to find the most active stations.
  * List the stations and observation counts in descending order.
  * Which station has the highest number of observations?
  * Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filter by the station with the highest number of observations.
  * Plot the results as a histogram with bins=12.

![Screen Shot 2021-08-27 at 2 05 25 PM](https://user-images.githubusercontent.com/19372031/131070438-7fec705f-c968-4dad-9ab9-dcc29d5e9390.png)

## Climate App
After the completed initial analysis, design a Flask API based on the queries that you have just developed.
* Use Flask to create your routes.

### Routes
* /
  * Home page.
  * List all routes that are available.
* /api/v1.0/precipitation
  * Convert the query results to a dictionary using date as the key and prcp as the value.
  * Return the JSON representation of your dictionary.
* /api/v1.0/stations
  * Return a JSON list of stations from the dataset.
* /api/v1.0/tobs
  * Query the dates and temperature observations of the most active station for the last year of data.
  * Return a JSON list of temperature observations (TOBS) for the previous year.
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

