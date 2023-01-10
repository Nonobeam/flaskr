import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from flask import Flask
import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def fptwebsite():
        return render_template("base.html")