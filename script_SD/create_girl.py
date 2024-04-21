import requests,base64,datetime,os,sys,time,random
import base as g

#画像作成メイン関数、基本的にいじらない。

def Main():
    # StableDiffusionURL
	url = g.url

	option_payload = {
		"sd_model_checkpoint": g.model,
		"sd_vae": g.vae,
	}

	response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

	# Create Picture
	Imgsetting = {
	# プロンプト
	"prompt": g.script,
	# ネガティブプロンプト
	"negative_prompt": g.negative,
	"steps": 30,
	"sampler_index":"DPM++ 2M",
	"width": width,
	"height": height,
	"cfg_scale": 7,
	"seed": -1,
	}
	resp = requests.post(url=f'{url}/sdapi/v1/txt2img', json=Imgsetting)
	json = resp.json()
	imgdata = json["images"][0]

	now = datetime.datetime.now()
	current_day = now.strftime("%Y-%m-%d")
	current_daytime = now.strftime("%Y%m%d%H%M%S")
	dir_for_output = "./output/" + current_day

	os.makedirs(dir_for_output, exist_ok=True)

	with open(f"{dir_for_output}/girl-{g.modelname}-{current_daytime}.png", "wb") as f:
		buf = base64.b64decode(imgdata)
		f.write(buf)
	return

# メインルーチン

if __name__ == '__main__':

	gazouchange = g.gazouchange

	# 画像大きさ指定(画像大きさ変更しない場合)
	width = g.width
	height = g.height

	# 引数確認(作成枚数)
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

	#計測開始
	start = time.perf_counter()

	# 繰り返し処理
	while i < n:

		#4枚ごとに大きさ変更する。
		if (i % 3 == 0 and gazouchange == 1 ):
			width = 512
			height = 512
		elif (i % 3 == 1 and gazouchange == 1 ):
			width = 512
			height = 768
		elif (i % 3 == 2 and gazouchange == 1 ):
			width = 768
			height = 512

		if (i < n):
			gazou = n - i
			print("画像はあと{}枚です。".format(gazou))

		Main()
		time.sleep(1)

		i = i + 1

	#計測終了
	end = time.perf_counter()
	jobtime1 = int((end-start)/60)
	jobtime2 = int((end-start)%60)

	print("画像作成完了しました。")
	print("作成時間は{}分{}秒です。".format(jobtime1,jobtime2))
