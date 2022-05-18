#!/bin/bash
# Script that takes in URL, adds header variable and displays body response
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
