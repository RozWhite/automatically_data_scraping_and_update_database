# automatically_data_scraping_and_update_database from a Website

This folder contains:
- Python code for automatically web crawling a web to find URLs or links from an open website (here the Trevisto website) that does not require a login.
- Python code for automatically web scraping of data from all URLs of an open website  and upload it to the Qdrant database.
- Code to detect new changes in a web site and automatically update the corresponding collection in the Qdrant database with the new scraped data.

--------------------------------------------------------------------------
## Version 1:
The first release script overview is described in the table below: 

| Version | Python file                     | description                                  |
|---------|---------------------------------|----------------------------------------------|
| 1       | config.py                       | Configuration file                           |
| 1       | get_Trevisto_Urls.py            | Finding all Urls in a Website                |
| 1       | extract_data_from_Urls.py       | Data extraction from URLs                    |
| 1       | autoupdate_qdrant_db.py         | Compare content and update database          |
----------------------------------------------------------------------------------------------
