# TICK Stack

Run the complete TICK stack using this [docker-compose](https://docs.docker.com/compose/) file.
By using docker-compose all four official TICK stack images are started and linked together.
To know more about the individual components see [this](https://influxdata.com/)

## Usage

Start all the  images as follows:

    # cd to desired version
    cd 0.11/
    # Start all images in the background
    docker-compose up -d

###Check that InfluxDB works:

Access the web inteface. [http://localhost:8083/](http://localhost:8083/)

####The `influx` client

Use the built-in influx cli service:

    docker-compose run influxdb-cli

###Check that Telegraf works

By default, the Telegraf creates a `telegraf` database.
Check that InfluxDB has such a database in addition to the `_internal` database.

    docker-compose run influxdb-cli
    > show databases

###Check that Chronograf works

Access the Chronograf inteface, [http://localhost:10000](http://localhost:10000)

You will need to add the InfluxDB server.
Use these settings:

Host: influxdb
Port: 8086

No auth or SSL.


###Check Kapacitor works

Use the built-in kapacitor cli service:

    docker-compose run kapacitor-cli
    $ kapacitor list tasks

Confirm Kapacitor is subscribed to all data in InfluxDB

    docker-compose run influxdb-cli
    > show subscriptions

## Supported Docker versions

This image is officially supported on Docker version 1.10.1
