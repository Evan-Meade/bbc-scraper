# bbc-scraper
Tutorial code for automatically scraping the top displayed headline on BBC News

Created by [Evan Meade](https://github.com/Evan-Meade), 2020 (MIT License)

This is a repository for code created for an article on setting up an automated web scraper. They are meant to demonstrate basic principles of grabbing web pages, searching for target content, and saving it to a central dataset. The files may appear a bit unrelated, but make sense in the context of the article.

## Contents

* **bbc.py** - contains a function for grabbing the top displayed headline on BBC News
* **example.html** - simple webpage which demonstrates HTML tag structure and attributes
* **headline_recorder.py** - grabs top headline on BBC News and appends it to a .csv file

## Setup

These scripts were developed in a Python3 virtual environment on an Ubuntu 18.04 system. It is recommended that you create your own virtual environment in the repository's base directory and activate it. Once you have, you can install all the necessary Python packages with

```
pip install -r requirements.txt
```

## Usage

The main functional script in this repository is `headline_recorder.py`, which appends the current top displayed headline on BBC News' website to `headlines.csv`. It can be executed with

```
python headline_recorder.py
```