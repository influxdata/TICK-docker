FROM debian:jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates apt-transport-https

RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 684A14CF2582E0C5 && \
    echo "deb https://repos.influxdata.com/debian jessie stable" > /etc/apt/sources.list.d/influxdata.list && \
    apt-get update

ENV INFLUXDB_VERSION 0.13.0-1
ENV TELEGRAF_VERSION 0.13.0-1
ENV CHRONOGRAF_VERSION 0.13.0
ENV KAPACITOR_VERSION 0.13.0-1
RUN apt-get install -y influxdb=$INFLUXDB_VERSION \
                       telegraf=$TELEGRAF_VERSION \
                       chronograf=$CHRONOGRAF_VERSION \
                       kapacitor=$KAPACITOR_VERSION

RUN apt-get install -y supervisor

ENV INFLUXDB_CONFIG /etc/influxdb/influxdb.conf
ENV TELEGRAF_CONFIG /etc/telegraf/telegraf.conf
ENV CHRONOGRAF_CONFIG /opt/chronograf/config.toml
ENV KAPACITOR_CONFIG /etc/kapacitor/kapacitor.conf

ENV PATH /opt/chronograf/:$PATH
ENV CHRONOGRAF_BIND 0.0.0.0:10000


EXPOSE 8083 8086 8088 8091 8125 8092 8094 10000 9092

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY listener.py /listener.py
COPY supervisordRunner.py /supervisordRunner.py
CMD ["/supervisordRunner.py"]
