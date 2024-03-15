import requests,base64,io,time,datetime,os

def Main():
	Imgsetting = {
	"prompt": "(masterpiece:1.1),(best quality:1.0),(super fine cel anime:1.2),cute girl,blouse,no background,flat background",
	"negative_prompt":"(worst quality, low quality:1.2),ugly,error,lowres,blurry,multipul angle, split view, grid view,text,signature,watermark,bad anatomy",
	"steps": 20,
	"sampler_index":"DPM++ 2M Karras",
	"width": 256,
	"height": 384,
	"cfg_scale": 7,
	"seed": -1,
	}
	resp = requests.post(url=f'http://192.168.11.33:7860/sdapi/v1/txt2img', json=Imgsetting)
	json = resp.json()
	imgdata = json["images"][0]
	
	now = datetime.datetime.now()
	current_day = now.strftime("%Y-%m-%d")
	current_time = now.strftime("%H-%M")
	dir_for_output = "./output/" + current_day

	os.makedirs(dir_for_output, exist_ok=True)

	with open(f"{dir_for_output}/{current_time}-{int(time.time())}.png", "wb") as f:
		buf = base64.b64decode(imgdata)
		f.write(buf)
	return

if __name__ == '__main__':
	Main()