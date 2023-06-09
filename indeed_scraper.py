from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import subprocess

# declaring variables for the program to run
val = 0
count = 0
# maximum number of jobs to be scraped
maximum_jobs = int(input("Enter the maximum number of jobs to be scraped: "))
job_name = input("Enter the job name: ")
location = input("Enter the location: ")
delete_file = input("Do you want to delete the existing file? (y/n): ")
shut_down = input("Do you want to shut down the computer after the program is completed? (y/n): ")

if delete_file == "y":
    with open('job.csv', 'w') as csv_file:
        csv_file.write("")

driver = webdriver.Chrome()
# declaring the minimum waiting time for the driver to wait for the page to load
driver.implicitly_wait(10)

# opening the indeed website
driver.get("https://in.indeed.com/?r=us")

# finding the search box and entering the job name
job_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input")
job_box.send_keys(job_name)

# finding the location box and entering the location
location_box = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[2]/div/div[1]/div/div[2]/input")
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
    # global count
    for job in jobs:
        try:
            a = job.find_element(By.TAG_NAME, "a")
            if val >= maximum_jobs:
                break
            elif a and job.text:
                href = a.get_attribute("href")
                # count += 1
                val += 1
                csv_writer(job.text,href)
        except Exception:
            continue
def shutdown_system():
    subprocess.run(["systemctl", "poweroff"])

# looping through the pages
while val < maximum_jobs:
    job = driver.find_element(by=By.XPATH, value="/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul")
    li_elements = job.find_elements(By.TAG_NAME, "li")
    get_job_info(li_elements)
    # val += count
    count = 0
    driver.get("https://in.indeed.com/jobs?q=software+engineer&l=India&fromage=1&start="+str(val+1))

# closing the driver
driver.quit()

# shutting down the computer
if shut_down == "y":
    shutdown_system()