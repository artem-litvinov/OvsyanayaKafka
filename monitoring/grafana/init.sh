#!/bin/sh

while ! curl -fsSL http://grafana:3000/api/dashboards/home 2>/dev/null 1>/dev/null ; do
    sleep 1
done

# create data source
curl -fsSL -H "Content-Type: application/json" \
    -d @/tmp/ds-prometheus.json \
    -XPOST \
    http://grafana:3000/api/datasources #|| true

# create docker dashboard
curl -fsSL -H "Content-Type: application/json" \
    -d @/tmp/docker-dashboard.json \
    -XPOST \
    http://grafana:3000/api/dashboards/db #|| true

# create monitoring dashboard
curl -fsSL -H "Content-Type: application/json" \
    -d @/tmp/docker-monitoring.json \
    -XPOST \
    http://grafana:3000/api/dashboards/db #|| true

# set default
curl -fsSL -H "Content-Type: application/json" \
    -d '{"theme":"","homeDashboardId":1,"timezone":""}' -XPUT \
    http://grafana:3000/api/org/preferences #|| true
