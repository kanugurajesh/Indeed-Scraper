from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()

# declaring variables for the program to run
val = 0
count = 0
maximum_jobs = 100
job_name = "Software Engineer"
location = "India"

# declaring the minimum waiting time for the driver to wait for the page to load
driver.implicitly_wait(10)

# opening the indeed website
driver.get("https://in.indeed.com/?r=us")

# finding the search box and entering the job name
job_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input")
job_box.send_keys(job_name)

# finding the location box and entering the location
location_box = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/div/div[2]/div/div[1]/div/div[2]/input")
location_box.send_keys(location)

# finding the search button and clicking it
text_search = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/button")
text_search.click()

# function to write the data to the csv file
def csv_writer(data,href):
    with open('job.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        splited_data = data.split("\n")
        writer.writerow(splited_data + [href])
    
# function to get the job information
def get_job_info(jobs):
    global count
    for job in jobs:
        try:
            a = job.find_element(By.TAG_NAME, "a")
            if a and job.text:
                print(job.text)
                href = a.get_attribute("href")
                print(href + "\n")
                count += 1
                csv_writer(job.text,href)
        except Exception:
            continue

# looping through the pages
while val < maximum_jobs:
    job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul")
    li_elements = job.find_elements(By.TAG_NAME, "li")
    get_job_info(li_elements)
    val += count
    count = 0
    driver.get("https://in.indeed.com/jobs?q=software+engineer&l=India&fromage=1&start="+str(val+1))

# closing the driver
driver.quit()