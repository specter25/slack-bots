import json
import requests
import csv

TOKEN='' #add your bots token

CHAT_ID= #add "-" before chat IDs for groups

URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

# def add_to_csv(message, 

def chat_id_and_text(updates):
    num_updates = len(updates["result"])
    for i in range(num_updates - 1, -1, -1):
        if updates["result"][i]["message"]["chat"]["id"] == CHAT_ID:
            try:
                entities=updates["result"][i]["message"]["entities"]
                for j in range (0,len(updates["result"][i]["message"]["entities"])):
                    if updates["result"][i]["message"]["entities"][j]["type"]== "url":
                        text = updates["result"][i]["message"]["text"].encode('ascii', 'ignore').decode('ascii')
                        text_entities = updates["result"][i]["message"]["entities"][0]["type"]
                        print(text, text_entities)
            except KeyError:
                print('no url')
                
chat_id_and_text(get_updates())

                           
