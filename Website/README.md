# automatically_data_scraping_and_update_database

This repository provides a method to automatically extract all URLs from a website and scrape all HTML data from each URL. Using crontab, this job is scheduled to run every day at a specific time. The content of the HTML files will be compared with the previous versions. If there are changes in the compared HTML files, the database will be updated automatically.

