from flask import Flask, render_template, request, url_for
import os
from thingspeak import Channel
import json
import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/form")

def form():
    return render_template("form.html")

@app.route("/Report", methods = ["GET","POST"])
def upload():
    if request.method == "POST":
        firstname= request.form.get("firstname")
        lastname = request.form.get("lastname")
        age = request.form.get("age")
        gender = request.form.get("gender")
        phone = request.form.get("phone")
        Email = request.form.get("email")
        about = request.form.get("about")
        dp = request.form.get("dp")
        img = request.files["dp"]
        img.save(f"C:/Users/User/PycharmProjects/smart_bed/static/images/{img.filename}")
        print(firstname)
        print(lastname)
        print(age)
        print(gender)
        print(phone)
        print(Email)
        print(about)
        print(dp)


        channel_id ="2307912"
        api_key = "JAG2GDYKXQFWJ92Z"
        # Define the ThingSpeak URL
        url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=100'




        # Fetch the data
        response = requests.get(url)

        # Parse the JSON response into a DataFrame
        data = response.json()
        df = pd.DataFrame(data['feeds'])

        # Print the data
        print(df)
        # Plot the data in a graph
        import matplotlib.pyplot as plt
        plt.subplots(figsize=(15, 5))
        plt.plot(df["field1"],c="green")
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title(' OXYGEN CONCENTRATION')
        plt.grid(True)
        # Save the graph as a PNG image
        plt.savefig('static/graph.png',transparent=True)

        plt.subplots(figsize=(15, 5))
        plt.plot(df["field2"], c="blue")
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('HEART RATE')
        plt.grid(True)
        # Save the graph as a PNG image
        plt.savefig('static/graph1.png', transparent=True)

        # Render the graph image in the HTML template
        return render_template('Report.html',firstname=firstname,lastname=lastname,age=age,about=about,img=dp,graph_url=url_for('static', filename='graph.png'),graph1_url=url_for('static', filename='graph1.png'))

if __name__ == '__main__':
    app.run(debug=True)