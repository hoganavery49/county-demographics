from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
    return render_template('home.html', options = get_state_options(counties))

@app.route("/fun-fact")
def render_fact():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    
    state = ""
    if 'state' in request.args:
        state = request.args["state"]
        
    funFact = fun_fact(counties, state)
    
    return render_template('fun-fact.html', fact = funFact)

def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def fun_fact(counties, state):
    mostSales = 0;
    county = ""
    for c in counties:
        if c["State"] == state and c["Sales"]["Retail Sales per Capita"] > mostSales:
            mostSales = c["Sales"]["Retail Sales per Capita"]
            county = c["County"]

    return "%s's county with the most retail sales per capita is %s at %i sales per capita" % (state, county, mostSales)

if __name__ =="__main__":
    app.run(debug=false, port=54321)
