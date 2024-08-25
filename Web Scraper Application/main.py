from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import re

def web_scraper(url, search_param, product):
    search_url = f"{url}{search_param}{product}"

    result = requests.get(search_url).text

    doc = BeautifulSoup(result, "html.parser")

    products = []

    for item in doc.find_all('div', class_="product-card"):
        

