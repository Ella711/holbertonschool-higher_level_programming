#!/bin/bash
# Script that takes in URL, adds post variables and displays body response
curl -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
