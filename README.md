# Selenium Web Scraper for Docker

I created this for developers looking to use Selenium's web driver to web scrape within a Docker. It is very useful for automating web scraping tasks using an external scheduler. The example provided in [app.py](https://github.com/rileycleavenger/SeleniumWebScraper-Docker/blob/main/src/app.py) allows for HTTP GET requests to be made to `<insert docker url>/<insert website to scrape url>` and returns a text file with the desired page's source code. Ideally this setup will just serve as an example for anyone looking to utlize Selenium and Docker in their webscraping processes.

## How To Use

### Command Line Initialization
```
git clone https://github.com/rileycleavenger/SeleniumWebScraper-Docker.git
```
```
cd SeleniumWebScraper-Docker/src
```
```
./build.sh
```

### Simple Scraping
using a web browser visit `/<insert website to scrape url>` to return a txt file with the page's source code
