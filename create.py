import requests,base64,datetime,os,sys

def Main():
    # StableDiffusionURL
	url = "http://IPアドレス:7860"

	# model select
	model = "モデル名"
	option_payload = {
    	"sd_model_checkpoint": model,
    	# "CLIP_stop_at_last_layers": 2
	}

	response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

	# Create Picture
	Imgsetting = {
	"prompt": "score_9,score_8_up,score_7_up BREAK source_anime,rating_explicit,(best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG, beautiful face, beautiful eyes, beautiful hair, kawaii:1.2),1girl,solo,long hair,green hair,blue eyes,tanned skin,beach,at midnight,arms up behind,kind_smile,portrait,medium breasts,casual",
	"negative_prompt":"(zPDXL,score_4,score_5,score_6,source_pony,source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),nsfw,nude",
	"steps": 30,
	"sampler_index":"DPM++ 2M Karras",
	"width": 1024,
	"height": 1024,
	"cfg_scale": 7,
	"seed": -1,
	}
	resp = requests.post(url=f'{url}/sdapi/v1/txt2img', json=Imgsetting)
	json = resp.json()
	imgdata = json["images"][0]

	now = datetime.datetime.now()
	current_day = now.strftime("%Y-%m-%d")
	current_daytime = now.strftime("%Y%M%H%M%S")
	dir_for_output = "./output/R18/" + current_day

	os.makedirs(dir_for_output, exist_ok=True)

	with open(f"{dir_for_output}/{current_daytime}.png", "wb") as f:
		buf = base64.b64decode(imgdata)
		f.write(buf)
	return

if __name__ == '__main__':
	
	# 引数確認
	i = 0
	if (len(sys.argv) == 2):
		args = sys.argv
		n = args[1]
		if(n.isdigit() == False):
			n = 1
		else:
			n = int(n)
	else:
		n = 1
	
	print("作成画像は{}枚です。".format(n))

	# 繰り返し処理
	while i < n:

		if (i < n):
			gazou = n - i
			print("画像はあと{}枚です。".format(gazou))

		Main()

		i = i + 1

	print("画像作成完了しました。")
