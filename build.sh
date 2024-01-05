#!/bin/bash

cd src
docker build -t us-central1-docker.pkg.dev/app/app-repo/app-scraper .
docker push us-central1-docker.pkg.dev/app/app-repo/app-scraper