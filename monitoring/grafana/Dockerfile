FROM alpine:3.4

ADD init.sh /init.sh
RUN chmod +x /init.sh
RUN apk update && apk add curl
ADD docker-monitoring.json docker-dashboard.json ds-prometheus.json /tmp/
CMD /init.sh
