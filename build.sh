#!/bin/bash

cd src
docker build --platform linux/amd64 -t my-python-app .
docker run -p 8080:8080 my-python-app