#!/bin/bash
cqlsh 10.0.1.40 --cqlversion="3.4.4" -f "${1}"
