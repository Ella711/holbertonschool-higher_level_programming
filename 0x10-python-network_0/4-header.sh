#!/bin/bash
# Script that takes in URL, adds header variable and displays body response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
