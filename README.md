# automatically_data_scraping_and_update_database

This repository provides a method to automatically extract all URLs from a Website/Sharepoint and scrape all HTML data from each URL. The content of the HTML files will be compared with the previous versions. If there are changes in the compared HTML files, the database will be updated automatically. With using the cronjob, this process is scheduled to run every day at a specific time.

### Overview 
The diagram below illustrates the process of the automated data pipeline used to extract all data from a website and update the database accordingly.

![Image](/demo.jpg)

###  Features 
**URL Extraction:** Automatically extract all URLs from a given website.<br />
**HTML Scraping:** Scrape HTML data from each extracted URL.<br />
**Content Comparison:** Compare the scraped HTML content with previous versions.<br />
**Automatic Database Update:** Update the database if changes are detected.<br />
**Scheduled Execution:** Use cronjob to schedule the job to run daily.<br />

## Coding Scenarios

This repository contains code for two different scenarios, each explained in its own folder:

**1. Accessing SharePoint Content:** This scenario explains how to access the content of a page on SharePoint that requires a login. See the [Sharepoint](/Sharepoint/) folder for details.<br />

**2. Accessing Open Website Content:** This scenario demonstrates how to access the content of an open website. See the [Website](/Website/) folder for details.<br />
 

## Cron Job 

Cronjob is a time-based job scheduler that allows tasks to be automatically run at scheduled times. <br /><br />
**Schedule the Python Script with Cron:**
- Run the follwing command in the Linux command line:
```
crontab -e
```
- Add a new cron job: 
```
30 8 * * * cd /home/yourusername/foldername && /usr/bin/python3 my_script.py
```
This line tells cron to run the Python script every day at 8:30 am.

If you are using a virtual environment, you should also activate that environment.

```
30 8 * * * cd /home/yourusername/foldername && source env/bin/activate && /usr/bin/python3 my_script.py
```
- Save and Exit
- To view the list of cron jobs that are scheduled, run:
```
crontab -l
```