import requests

url = "https://www.tmsandbox.co.nz/Members/Listings.aspx?member="
start_userid = 4000705

for i in range(500):
    new_id = start_userid + i
    response = requests.get(url + str(new_id))
    start_username = response.text.find('/Members/Listings.aspx?member=') + 39
    # print(response.text[start_username:start_username+200])
    end_username = response.text[start_username:].find("</a>")
    username = response.text[start_username:end_username+start_username]
    print(f"{new_id} : {username}")
