# StableDiffusionURL
url = "http://IPアドレス:7860"

# 特定の枚数の作成指定の際の画像変化許可
# 3で4枚ごとに許可、4で6枚ごとに許可、
# 2で2枚ごとに許可、1で9枚ごとに許可、0で許可しない。
gazouchange = 0

# 0で許可しない場合の画面大きさ
width = 896
height = 1152

vae = "VAE名"

model = "モデル名"
modelname = "モデル名(出力ファイルに入れる名称)"

script = "(score_9, score_8_up, score_7_up, BREAK source_anime, rating_explicit), (best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG,beautiful face, beautiful eyes, beautiful hair, kawaii),(1girl,solo), blue hair,long hair,straight hair,red eyes,long eyelashes,drooping eyes,mediun breasts,school_uniform,skirt,street,full body,standing"

negative = "(zPDXL,score_4,score_5,score_6,source_pony),(source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),(nsfw,nude,nippless,public hair,revealing clothes,bed,on bed,bed room,private parts,take off clothes)"