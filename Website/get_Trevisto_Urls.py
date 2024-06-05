import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
#from urllib.request import urlopen, Request 

#### 1- get all Urls from the first pages
def get_all_urls(base_url):
    # Send GET request to the base URL
    response = requests.get(base_url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all anchor tags (links) from the page
        links = soup.find_all('a')

        # List to store all URLs
        all_urls = []

        # Iterate through each link
        for link in links:
            #print(link)

            #if "https://www.trevisto.de/" in  link.get('href'):
            # Get the value of the 'href' attribute
                href = link.get('href')
    
                # Check if 'href' attribute ends with ('/')
                if href.endswith("/"):
                    href=href[:-1]
                    #print('inside', href)
                    
                # Join the base URL with the href to create the absolute URL
                #print('### outside: ', href)
                absolute_url = urljoin(base_url, href)
    
                # Append the absolute URL to the list
                all_urls.append(absolute_url)

        return all_urls
    else:
        # Print error message if request fails
        print("Failed to retrieve data from the website.")
        return None

base_url = "https://www.trevisto.de"
all_urls = get_all_urls(base_url)
urls_first=list(dict.fromkeys(all_urls))
urls_first= [element for element in urls_first if base_url in element ]
# print(urls_first)

#### 2- Just loop over Stellenangebote URL to extract all the urls there. 
base_url = "https://www.trevisto.de/karriere/stellenangebote"
all_urls = get_all_urls(base_url)
urls_stell=list(dict.fromkeys(all_urls))


result= list(set(urls_first) | set(urls_stell))
sub = 'https://www.trevisto.de/'
#sub1='-m-w-d'
sub1="top"
urls = [element for element in result if sub in element and sub1 not in element]
#urls = [element for element in result if sub in element ]
#print(len(urls))
# print(urls)

############################################################################################################################

# ####  There are some old urls from "news" or "references" which we do not need their information in our chatbot. So we just need to loop over the career url in step 2.
# # In case you want to get all urls from a website, run the code below in step 2 instead. 

# def get_list_urls():
#     alls = []

#     for i in range(len(urls_first)):
#     # Send GET request to the each  URLS
#             response = requests.get(urls_first[i])
        
#             # Check if request was successful
#             if response.status_code == 200:
#                 # Parse HTML content using BeautifulSoup
#                 soup = BeautifulSoup(response.content, 'html.parser')
                
#                 # Extract all anchor tags (links) from the page
#                 links = soup.find_all('a')
#                 #alls = []
                
         
#                 # Iterate through each link
#                 for link in links:
#                     #print(link)
#                     # Get the value of the 'href' attribute
#                     href = link.get('href')
#                     if href is not None and "https://www.trevisto.de/" in  href and 'https://www.trevisto.de/media' not in href and "https://www.trevisto.de/advanced-analytics" not in href:
                        
#                         # Check if 'href' attribute ends with ('/')
#                         if href.endswith("/"):
#                             href=href[:-1]
#                             #print('inside', href)
                            
#                         # Join the base URL with the href to create the absolute URL
#                         #print('### outside: ', href)
#                         absolute_url = urljoin(base_url, href)
            
#                         # Append the absolute URL to the list
#                         alls.append(absolute_url)
#                 #return alls
#             else:
#                 # Print error message if request fails
#                 print("Failed to retrieve data from the website.")
#                 return None
#     return alls

# # Example usage
# base_url = "https://www.trevisto.de"
# all_urls = get_list_urls()
# urls=list(dict.fromkeys(all_urls))
# print(len(urls))
