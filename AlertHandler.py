import requests

url = "https://webhook.site/45386ce0-3a23-4051-830c-cff7c560de95"
host = "185.139.25.6"
id = "1ff72efd-36ac-45cb-858d-e53a642a4180"


def SendAlertMessage(alerts):
    for currency in alerts:
        if True == alerts[currency]:
            json = {"defualt_status": 200,
                    "default_content": currency + " has shifted more than 0.0005",
                    "default_content_type" : "text/html",}

            headers = {"api-key" : "00000000-0000-0000-0000-000000000000"}

            r = requests.post(url, json= json, headers= headers)
            # print(r.json["uuid"])
