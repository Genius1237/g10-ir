#!/bin/bash

export PYTHONPATH=$(pwd)/bleak-0.22.2:$(pwd)/dbus-fast-2.22.1/src
python run.py $1
