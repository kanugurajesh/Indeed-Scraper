import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# ...
val = 1
maximum_jobs = 100
job_name = "Software Engineer"

driver.implicitly_wait(10)
driver.get("https://in.indeed.com/?r=us")

text_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input")
text_box.send_keys(job_name)

text_search = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/button")
text_search.click()

def get_job_info(jobs):
    for job in jobs:
        try:
            a = job.find_element(By.TAG_NAME, "a")
            if a:
                print(job.text)
                href = a.get_attribute("href")
                print(href + "\n\n")
        except Exception:
            continue

if val == 1:
    # job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/nav/div[6]/a")
    # job.click()
    # time.sleep(3)
    job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul")
    li_elements = job.find_elements(By.TAG_NAME, "li")
    get_job_info(li_elements)
    val += 1

if val == 2:
    # job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/nav/div[7]/a")
    driver.get("https://in.indeed.com/jobs?q=software+engineer&l=India&fromage=1&start=2")
    if val==2:
        turn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/button")
        turn.click()
    # job.click()
    time.sleep(3)
    job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul")
    li_elements = job.find_elements(By.TAG_NAME, "li")
    get_job_info(li_elements)
    val += 1

while val < maximum_jobs:
    # job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/nav/div[7]/a")
    # job.click()
    driver.get("https://in.indeed.com/jobs?q=software+engineer&l=India&fromage=1&start="+str(val))
    time.sleep(3)
    job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul")
    li_elements = job.find_elements(By.TAG_NAME, "li")
    get_job_info(li_elements)
    val += 1

driver.quit()