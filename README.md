# Jupyter Notebook
## Mars News
Used Jupyter notebook to create a Python script to scrape the Mars News Site to grab the title and paragraph text.
## JPL Mars Space Images
Scraped the featured image and saved the image URL.
## Mars Facts
Used Pandas to scrape a table of information and converted the data into an HTML table string.
## Mars Hemispheres
Grabbed the image URLs of the 4 hemispheres of Mars and their respective names, saving them both as Python dictionaries for each hemisphere, and appended those 4 dictionaries into a list.
# MongoDB and Flask App
Created a web page that displays all of the scraped data in a custom HTML template.
* Converted Jupyter notebook into a python script that used a scrape() function that ran the whole code and returned a python dictionary of all data.
* Created a flask app that imported and ran the scraping code and stored the returned python dictionary into MongoDB.
* Created a root route that queries MongoDB and passes the Mars data into an HTML template.
* Created an index.html file that takes the Mars data dictionary and displays it all in HTML format.
