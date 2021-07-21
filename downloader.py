# Download and save file from internet
# Author Rocken2k

import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)

download("") # <------------ URL location 

