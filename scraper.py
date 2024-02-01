import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        page_content = response.content

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find all job postings
        jobs = soup.find_all('article')

        # Create a list to store the job details
        job_list = []

        # Loop through the list of jobs and get the details
        for job in jobs:
            title = job.find('a', {'data-automation': 'jobTitle'}).text
            company = job.find('a', {'data-automation': 'jobCompany'}).text
            location = job.find('a', {'data-automation': 'jobLocation'}).text
            job_list.append((title, company, location))

        return job_list

# URL of the page you want to scrape
url = "https://www.seek.co.nz/jobs-in-information-communication-technology/in-Christchurch-Canterbury"

# Call the function and print the jobs
jobs = scrape_jobs(url)


# Specify the CSV file name
csv_file = "jobs_data.csv"

# Write the data to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Title', 'Company', 'Location'])

    # Write the job details
    writer.writerows(jobs)

print(f"Data has been written to {csv_file}")