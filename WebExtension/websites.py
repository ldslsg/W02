import requests
from bs4 import BeautifulSoup
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_ = "jobs").find_all('li')[1:-1]

for job in jobs:
    title = job.find("span", class_="title").text

    company, position, region = job.find_all("span", class_="company")[0:3]
    company = company.text
    position = position.text
    region = region.text
    print(f"title : {title} company : {company} position : {position} region : {region}")

print(jobs)
# websites = (
#     "Google.com",
#     "airbnb.com",
   
#     "https://Facebook.com"
# )

# results = {}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     code = get(website).status_code
#     if code >= 500:
#         results[website] = "5xx / server error"
#     elif code >= 400:
#         results[website] = "4xx / client error"
#     elif code >= 300:
#         results[website] = "3xx / redirection "
#     elif code >= 200:
#         results[website] = "2xx / successful"
#     elif code >= 100:
#         results[website] = "1xx / informational response"

# print(results)