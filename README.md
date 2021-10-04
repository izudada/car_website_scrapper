# A Web Scrapping Technical Assessment 

##Usecase

To get/scrape information of cars on  [base_url](https://www.edmunds.com/cars-for-sale-by-owner/).
These informations include:
- Name
- Price
- VIN Number
- Vehicle Summary
- Top Features & Specs

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/car_website_scrapper.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
Change directory with
```sh
    cd edmunds_scraper
```

```sh
scrapy crawl edmunds -o filename.xlsx
```

## Note 

You need to be connected to the internet to successfully scrape all data into yoor excel file. This process takes 30mins or less to complete.

Enjoy your experience