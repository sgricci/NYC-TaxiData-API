DROP TABLE IF EXISTS `borough_lookup`;
CREATE TABLE `borough_lookup` (
    `borough_id` int(10) not null,
    `name` varchar(200) not null,
    PRIMARY KEY (`borough_id`)
);

DROP TABLE IF EXISTS `trip_summary`;
CREATE TABLE `trip_summary` (
  `vendor_type` enum('yellow','fhv','green') NOT NULL,
  `trip_date` datetime NOT NULL,
  `pickup_borough` int(10) NOT NULL,
  `dropoff_borough` int(10) NOT NULL,
  `number_of_trips` int(10) NOT NULL,
  `elapsed_time_min` int(10) NOT NULL,
  `total_distance` int(10) NOT NULL,
  `total_amount` int(10) NOT NULL,
  `total_tips` int(10) NOT NULL,
  `average_time` int(10) NOT NULL,
  `average_distance` int(10) NOT NULL,
  `average_amount` int(10) NOT NULL,
  PRIMARY KEY (`vendor_type`,`trip_date`,`dropoff_borough`,`pickup_borough`),
  KEY `idx_trip_data_pickup_borough_dropoff_borough` (`pickup_borough`,`dropoff_borough`),
  KEY `idx_trip_data_pickup_time_dropoff_time` (`trip_date`),
  KEY `idx_time_and_boroughs` (`trip_date`,`pickup_borough`,`dropoff_borough`),
  KEY `idx_trip_data_vendor_type_pickup_time_dropoff_time` (`vendor_type`,`trip_date`),
  KEY `idx_trip_data_vendor_type_pickup_borough_dropoff_borough` (`vendor_type`,`pickup_borough`,`dropoff_borough`),
  KEY `idx_type_time_borough` (`vendor_type`,`trip_date`,`pickup_borough`,`dropoff_borough`)
);
