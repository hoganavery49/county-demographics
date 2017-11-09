from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html', options = get_state_options(counties))

@app.route("fun-fact")
def render_fact():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
    fact = fun_fact(counties, )

def get_state_options(counties):
    options = ""
    for c in counties:
        options += Markup("<option value=\"" + counties["State"] + "\">" + counties["State"] + "</option")
    return options

def fun_fact(counties, state):
    mostSales = 0;
    county = ""
    for c in counties:
        if c["State"] == state and c["Sales"]["Retain Sales per Capita"] > mostSales:
            mostSales = c["Sales"]["Retain Sales per Capita"]
            county = c["County"]

    return [county, mostSales]

if __name__ =="__main__":
    app.run(debug=false, port=54321)