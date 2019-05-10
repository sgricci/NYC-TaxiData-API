# New York City - Taxi Data API

NYC-TaxiData-API is an API built in Flask/Python (3) and MySQL utilizing the [New York City transporation data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) to summarize the data and provide useful metrics about past For-Hire Vehicle and Taxi transporation between the 5 boroughs of New York.

# Requirements

* Python 3 (tested with 3.7.3 and 3.6)
* A MySQL Server
* pip

# Development Setup

> These commands are tested on Arch and Manjaro Linux, and should work on Mac OS X, or [Ubuntu on Windows](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0). If you are using Windows shell, you should make sure MySQL and Python are in your PATH.

Here are the steps for setting up your local development environment:

1. Clone the repository

```bash
$ git clone git@github.com:sgricci/NYC-TaxiData-API.git
$ cd NYC-TaxiData-API
```

2. Import the database

```bash
$ mysqladmin -u root create TaxiData
$ mysql -u root TaxiData < app/data/data.sql
```

> Note: change 'root' in the above commands to whatever user you use for mysql. You can also add '-p <password>' if you have a password on your local mysql

3. Setup virtualenv

```bash
$ cd src/
$ python3 -m venv venv
```

4. Activate venv

```bash
$ . venv/bin/activate
```

> If you are using fish, or csh, you can replace 'activate' with 'activate.fish' or 'activate.csh'


5. Install from requirements.txt
```bash
$ pip install -r requirements.txt
```

# Running

> Use the `DATABASE_URL` environment variable to set up your python connection string

Bash:
```bash
$ cd src/
$ DATABASE_URL="mysql://root@localhost/TaxiData" python3 ./run_dev.py
```

Fish:
```fish
$ cd src/
$ env DATABASE_URL="mysql://root@localhost/TaxiData" python3 ./run_dev.py
```

Then open your browser to http://localhost:5000/ and enjoy.


# Running Tests

```bash
$ cd src/
$ pytest
```

# API

## Endpoints

### Boroughs

```http 
GET /boroughs
```

This endpoint will return a list of boroughs and their corresponding IDs.

*No parameters required.*

### Trips

```http
GET /trips
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `from_borough` | `int` | A Borough ID from the `/boroughs` endpoint This will filter the data by origin |
| `to_borough` | `int` | A Borough ID from the `/boroughs` endpoint. This will filter the data by destination |
| `type` | `string` | One of `green`, `yellow`, `fhv`. This will filter the data by the ride type / vehicle type |
| `from` | `date` | A date (and optional time), formatted in YYYY-MM-DD HH:II:SS format (i.e. 2018-01-02 06:30:57). |
| `to` | `date` | A date (and optional time), formatted in YYYY-MM-DD HH:II:SS format (i.e. 2018-01-02 06:30:57). |



```
# Type example:
GET /trips/<type>?from=2018-01-01&to=2018-01-07

# Fully loaded example:
GET /trips/<from_borough>/<to_borough>/<type>?from=2018-01-01&to=2018-01-07
```

## Responses

### Example
```js
{
  "data": [
        {
      "average_amount": 12.3, 
      "average_distance": 2.31, 
      "average_time": 13.87, 
      "dropoff_borough": 4, 
      "elapsed_time_min": 13, 
      "number_of_trips": 1, 
      "pickup_borough": 4, 
      "total_amount": 12.3, 
      "total_distance": 2.31, 
      "total_tips": 0.0, 
      "trip_date": "Thu, 05 Apr 2018 04:00:00 GMT", 
      "type": "green"
    }
  ], 
  "length": 1, 
  "status": 200
}
```

### Format
| Field | Type | Description
| :--- | :--- | :--- |
| `data` | `array` | The payload of data |
| `length` | `int` | number of record returned |
| `status` | `int` | HTTP response code (i.e. 200 OK, or 404 Not Found) |