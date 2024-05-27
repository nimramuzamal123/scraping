import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.digitale-wegbereiter.de/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text_elements = soup.find_all(text=True)
filtered_text_elements = [element for element in text_elements if 
                          element.parent.name not in ["script", "style"] and not 
                          element.parent.has_attr("class") and not 
                          element.parent.has_attr("id")]

with open("website_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Text Data"])
    writer.writerows([[text] for text in filtered_text_elements])
