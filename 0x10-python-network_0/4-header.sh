#!/bin/bash
# Script that takes in URL, adds header variable and displays body response
curl -sX "GET" -H "X-HolbertonSchool-User-Id":98 "$1"
