# Pandas - Alex Liu and Ivan Zhang
# SoftDev1 pd07
# K #10: Jinja Tuning ...
# 2018-09-21

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
