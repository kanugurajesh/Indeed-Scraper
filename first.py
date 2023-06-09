# import requests
# from bs4 import BeautifulSoup

# def extract(page):
#     headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
#     url = f"https://in.indeed.com/jobs?q=software+engineer&l=&vjk=57d256c7b6be3f36&start={page}"
#     r = requests.get(url, headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     return soup

# def transform(soup):
#     divs = soup.find_all('div', class_ = 'job_seen_beacon')
#     return len(divs)

# c = extract(0)
# print(transform(c))

# import requests
# from bs4 import BeautifulSoup

# def extract(page):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
#     url = f"https://in.indeed.com/jobs?q=software+engineer&l=&vjk=57d256c7b6be3f36&start={page}"
#     r = requests.get(url, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     return soup

# def transform(soup):
#     divs = soup.find_all('div', class_='job_seen_beacon')
#     return len(divs)

# c = extract(0)
# print(transform(c))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract(page):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    url = f"https://in.indeed.com/jobs?q=software+engineer&l=&vjk=57d256c7b6be3f36&start={page}"
    driver.get(url)
    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job_seen_beacon')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    return len(divs)

c = extract(0)
print(transform(c))
