from  import response
import requests

url = "https://www.tmsandbox.co.nz/home-living/lounge-dining-hall/other/listing-"
idnum = 2149451448
suffix = ".htm"


for i in range(5):
    new_id = idnum + i
    response = requests.get(url + str(new_id) + suffix)
    start_title = response.text.find("<title>") + 7
    end_title = response.text.find("</title>")
    title = response.text[start_title:end_title]
    print(f"{new_id} : {title}")