# Thoughts

> Using this to document my thought process 
during the 3 hour development time of this code.

## Initial Thoughts (Pre-Code) / Plan of attack

Write a quick API using Python / Flask / MySQL. It looks
like a lot of data, so possibly a quick script (PHP, because the position requires
us to work in the stack of the client, and multiple languages might be bonus points?)
to summarize the data into hourly summary rows

Should save time for unit tests and documentation

### Requirements

*   We can filter based on yellow cab, green cab, and for-hire vehicle.
*   We can provide a start and end borough for our trip.
*   We can filter based on datetime.
*   The returned data shows some interesting metrics that will help us get around.
*   Your code is well-tested.
*   Documentation is provided for how to build and run your code.


### Plan of Attack

* Grab data
* Code Shell of an API using Flask
* Create Two endpoints
	* Boroughs
	* TripData?
* Write sample SQLite database
* Write unit tests / test harness
* Write data summarization tool
* Write documentation while data summarization tool works
* Test

### Interesting Metrics

- Cost per unit of distance
- Average trip cost
- Average distance
- Average duration


## Start of work 


