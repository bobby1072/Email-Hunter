import requests
import json
#import pymongo
def mail_finder(url) -> str:
    emails = requests.get(f"https://api.hunter.io/v2/domain-search?domain={url}&api_key=471f9541c4b25249df0143940d3cf6d0b3331680")
    jsan = json.loads(emails.text)
    email_arr =[]
    info ={}
    #client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser@cluster0.sssd1.mongodb.net/?retryWrites=true&w=majority")
    #colection = client["email_store"]["emails"]
    for email in jsan["data"]["emails"]:
        email_arr.append(email["value"])
        sett = {
                "email": email["value"],
               "first_name": email["first_name"],
               "last_name": email["last_name"],
               "phone_number":email["phone_number"]
               }
        info[str(email["value"])] = sett
    post = {"organisation": jsan["data"]["organization"],
            "emails": info
            }
    #if post["organisation"] != None:
        #colection.insert_one(post)
    return email_arr