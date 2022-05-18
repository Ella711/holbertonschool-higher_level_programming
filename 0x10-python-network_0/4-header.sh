#!/bin/bash
# Script that takes in URL, adds header variable and displays body response
curl -s -X GET "$1" -H "X-School-User-Id: 98"
