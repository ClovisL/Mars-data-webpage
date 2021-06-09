#!/usr/bin/env python
# coding: utf-8


from splinter import Browser
from bs4 import BeautifulSoup as Soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    #Splinter setup
    executablepath = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executablepath, headless=False)


    # Nasa Mars News Site

    #Go to the URL for the news site
    url = "https://www.redplanetscience.com"
    browser.visit(url)

    #Create a Soup object
    html = browser.html
    news_soup = Soup(html, "html.parser")

    #Find the list text
    element = news_soup.select_one("div.list_text")


    #Find the news title
    news_title = element.find("div", class_="content_title").get_text()


    news_paragraph = element.find("div", class_="article_teaser_body").get_text()


    # JPL Mars Space Images

    #Go to the URL for the images site
    url = "https://www.spaceimages-mars.com"
    browser.visit(url)

    html = browser.html


    #Find the image button
    image_element = browser.find_by_tag("button")[1]
    image_element.click()


    #After clicking the image
    #Create a Soup object
    html = browser.html
    image_soup = Soup(html, "html.parser")


    #Find the image URL
    image_url = image_soup.find('img', class_='fancybox-image').get('src')


    img_url = f"{url}/{image_url}"


    # Mars Facts

    #Use Pandas to read the page
    df = pd.read_html("https://www.galaxyfacts-mars.com")[0]
    df


    #Re-configure the data frame
    df.columns = ["Description", "Mars", "Earth"]
    df.set_index("Description", inplace=True)
    df

    facts = df.to_html()


    # Mars Hemispheres

    #Go to the URL for the images site
    url = "https://www.marshemispheres.com"
    browser.visit(url)

    html = browser.html


    #Create a list to hold images and titles
    hemisphere_urls = []

    links = browser.find_by_css("a.product-item img")
    for link in range(len(links)):
        hemisphere_dict = {}
        
        #Click the picture
        browser.find_by_css("a.product-item img")[link].click()
        
        #Find the text marked "sample"
        sample = browser.links.find_by_text("Sample").first
        #Find href
        hemisphere_dict["img_url"] = sample["href"]
        
        #Find headings and store them as titles
        hemisphere_dict["title"] = browser.find_by_css("h2.title").text
        
        #Append dictionary to list of URLs
        hemisphere_urls.append(hemisphere_dict)
        
        #Go back to main page
        browser.back()


    print(hemisphere_urls)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "mars_img": img_url,
        "mars_facts": facts,
        "hem_urls": hemisphere_urls
    }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data



