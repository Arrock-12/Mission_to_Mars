# Mission_to_Mars

## Overview

For this project we used Splinter and Beautiful Soup to scrape data from the internet about Mars and store that information in MongoDB. We then used Flask to create a web app that ran the scraping tool and rendered it into a mobile-responsive html page.

## Resources

- Data Source: Mission_to-Mars_Challenge.ipynb, scraping.py, app.py, index.html
- Software: MongoDB 5.0.9, Python 3.7.11, VS Code 1.68.1, Flask 1.1.2

## Results

For this project we scraped data from the internet and stored it in MongoDB. We then wrote a Flask app that would pull the scraped data and display it on an html webpage designed with Bootstrap 3.

![Hemispheres](https://user-images.githubusercontent.com/101822948/175431527-053444c8-2634-4205-bb24-d06a000a4e69.png)


In the initial project we used Jupyter notebook to write code to scrape the most recent headline and synopsis from the NASA website redplanetscience.com.

We then scraped the featured image from spaceimages-mars.com to display on the webpage.

We then used the Pandas function read_html to copy a table from galaxyfacts-mars.com that we could then mirror on our webpage.

Finally, using Splinter and Beautiful Soup we visited the website marshemispheres.com and instructed Splinter to click on links so that we could scrape the urls for the full size images of the hemispheres and pull the titles.

![Mars_hemis_func](https://user-images.githubusercontent.com/101822948/175431376-322fad3d-8da8-4171-a2f1-38776ea7a901.png)

Using VS Code, we created a Flask app called app.py that would automate the scraping function with a button click and use the information stored on MongoDB to populate the webpage with the most current news headline, a synopsis of the news story, the featured image, a table of Mars to Earth comparisons, and images of the four hemispheres.


![app](https://user-images.githubusercontent.com/101822948/175431359-63db1c04-e3e3-4aef-b621-f3f807540d59.png)


By running the app.py code and copying the Flask url we were able to see the Mission to Mars website we created as well as update it by clicking the button.

Finally, we updated the html code to increase visual appeal. I changed the color of the button and made the headline bold. In addition I centered all the other headlines to improve readability. I also ensured that the webpage was mobile responsive by using the Toggle Device toolbar.


![Webpage_thumbnails](https://user-images.githubusercontent.com/101822948/175431332-2e143f18-1bb8-40cb-b6b8-c84507141cc2.png)

