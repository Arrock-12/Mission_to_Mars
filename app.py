from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    # Find one record of data from the mongo db
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    # Run the scrape function
    mars_data = scraping.scrape_all()

    # Update the Mongo db using update and upsert = True
    mars.update_one({}, {"$set":mars_data}, upsert=True)

    # Redirect back to index, issue code if not found
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)