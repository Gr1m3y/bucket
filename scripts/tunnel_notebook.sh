#!/usr/bin/env bash
# Author: Angus S. Hilts
# Date: 13-07-2021
# Desc:
#   One liner to start a tunnel over SSH for accessing a remote jupyter 
#   notebook or other server hosted on localhost at port 8080

HOST=$1

ssh -N -L 8080:localhost:8080 ${HOST}
