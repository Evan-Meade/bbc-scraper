# bbc-scraper
Tutorial code for automatically scraping the top displayed headline on BBC News

Created by [Evan Meade](https://github.com/Evan-Meade), 2020 (MIT License)

This is a code repository for an article on how to setup an automated web scraper. These scripts are meant to demonstrate the basic principles of grabbing web pages, searching for target content, and saving it to a central dataset. The files may appear a bit unrelated, but make sense in the context of the article. The tutorial also covers how to setup this code as an automated command (cron job) on a virtual machine, so that headlines can be collected without the need for user intervention.

## Contents

* **bbc.py** - contains a function for grabbing the top displayed headline on BBC News
* **example.html** - simple webpage which demonstrates HTML tag structure and attributes
* **headline_recorder.py** - grabs top headline on BBC News and appends it to a .csv file

## Setup

These scripts were developed in a Python3 virtual environment on an Ubuntu 18.04 system. It is recommended that you create your own virtual environment in the repository's base directory and activate it. Once you have, you can install all the necessary Python packages with

```
pip install -r requirements.txt
```

Then, you need to update the file path for the `OUTPUT_FILE`. This can be done by manually changing line 5 in `headline_recorder.py`. Put in the absolute path, especially if you plan on running this as a cron job (ie. use `/home/evan/bbc-scraper/headlines.csv` instead of just `headlines.csv`). While it is recommended that you put the output file in the same base directory as this repository, you can really put it anywhere on your system depending on your needs.

## Usage

The main functional script in this repository is `headline_recorder.py`, which appends the current top displayed headline on BBC News' website to `headlines.csv`. It can be executed with

```
python headline_recorder.py
```