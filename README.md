# automatically_data_scraping_and_update_database

This repository provides a method to automatically extract all URLs from a website and scrape all HTML data from each URL. Using crontab, this job is scheduled to run every day at a specific time. The content of the HTML files will be compared with the previous versions. If there are changes in the compared HTML files, the database will be updated automatically.

### Overview 
The diagram below illustrates the process of the automated data pipeline used to extract all data from a website and update the database accordingly.

![Image](/demo.jpg)

###  Features 
**URL Extraction:** Automatically extract all URLs from a given website.<br />
**HTML Scraping:** Scrape HTML data from each extracted URL.<br />
**Scheduled Execution:** Use crontab to schedule the job to run daily.<br />
**Content Comparison:** Compare the scraped HTML content with previous versions.<br />
**Automatic Database Update:** Update the database if changes are detected.<br />