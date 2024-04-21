import requests
from pprint import pprint

def Main():

    with open("output/sd_vae.txt", '+w', encoding='UTF-8') as f:
        f.write('\n'.join(sd_vae))

if __name__ == '__main__':

    url = "http://IPアドレス:7860"
    sd_vae = requests.get(f"{url}/sdapi/v1/sd-vae").json()
    sd_vae = [i["model_name"] for i in sd_vae]
    Main()
