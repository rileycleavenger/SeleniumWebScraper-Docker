#!/bin/bash

cd src
docker build --no-cache --platform linux/amd64 -t my-python-app .
docker run -p 8080:8080 --memory=8g --cpus=1 my-python-app