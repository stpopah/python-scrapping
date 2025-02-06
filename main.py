import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

ads = soup.find_all("li", class_="feature--ad")
for ad in ads:
    ad.decompose()

jobs = soup.find("section", class_="jobs").find_all("li")

for job in jobs:
    title = job.find("h4", class_= "new-listing__header__title").text
    company_name = job.find("p", class_= "new-listing__company-name").text
    print(title, "========", company_name)