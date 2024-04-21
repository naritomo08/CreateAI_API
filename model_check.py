import requests
from pprint import pprint

def Main():

    # Model List Create
    with open("output/sd_model.txt", '+w', encoding='UTF-8') as f:
        f.write('\n'.join(sd_models))

if __name__ == '__main__':

    url = "http://IPアドレス:7860"
    sd_models = requests.get(f"{url}/sdapi/v1/sd-models").json()
    sd_models = [i["title"] for i in sd_models]
    # Main Rouchin
    Main()
