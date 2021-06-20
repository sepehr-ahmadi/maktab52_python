#!/bin/bash
echo "Enter the location latitude: "
read latitude
echo "Enter the locaiton longitude"
read longitude
echo sunrise
curl -s $( "https://api.sunrise-sunset.org/json?lat=$latitude&lng=$longitude")| python -c "import sys, json; print json.load(sys.stdin)['results']['sunrise']"
echo sunset
curl -s $( "https://api.sunrise-sunset.org/json?lat=$latitude&lng=$longitude")| python -c "import sys, json; print json.load(sys.stdin)['results']['sunset']"
