# automatically_data_scraping_and_update_database

This repository provides a method to automatically extract all URLs from a Website/ Sharepoint and scrape all HTML data from each URL. Using crontab, this job is scheduled to run every day at a specific time. The content of the HTML files will be compared with the previous versions. If there are changes in the compared HTML files, the database will be updated automatically.

### Overview 
The diagram below illustrates the process of the automated data pipeline used to extract all data from a website and update the database accordingly.

![Image](/demo.jpg)

###  Features 
**URL Extraction:** Automatically extract all URLs from a given website.<br />
**HTML Scraping:** Scrape HTML data from each extracted URL.<br />
**Scheduled Execution:** Use crontab to schedule the job to run daily.<br />
**Content Comparison:** Compare the scraped HTML content with previous versions.<br />
**Automatic Database Update:** Update the database if changes are detected.<br />

## Coding Part

text 

## Cron Job 
Cronjob is a time-based job scheduler that allows tasks to be automatically run at scheduled times. <br /><br />
**Schedule the Python Script with Cron:**
- Write 'crontab -e' in the Linux command line
- Add a new cron job: 
```
0 * * * * cd /home/yourusername/foldername && /usr/bin/python3 my_script.py
```
This line tells cron to run the Python script every hour at the start of the hour.

If you are using a virtual environment, you should also activate that environment.

```
0 * * * * cd /home/yourusername/foldername && source env/bin/activate && /usr/bin/python3 my_script.py
```
