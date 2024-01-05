#!/bin/bash

cd src
docker build -t my-python-app .
docker run -p 8080:8080 my-python-app