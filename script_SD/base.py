# StableDiffusionURL
url = "http://IPアドレス:7860"

# 特定の枚数の作成指定の際の画像変化許可
# 1で正方形、縦長、横長に変化、0で変更を許可しない。
gazouchange = 0

# 0で許可しない場合の画面大きさ
width = 512
height = 768

vae = "VAE名"

model = "モデル名"
modelname = "モデル名(出力ファイルに入れる名称)"

script = "/* ベースライン */, (score_9, score_8_up, score_7_up, BREAK source_anime, rating_explicit), (best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG,beautiful face, beautiful eyes, beautiful hair, kawaii), /* ソロ */, (1girl,solo), /* random girl */,{blue|yellow|red|black|pink|purple} hair,{long|short} hair,straight hair,{blue|yerrow|red|black|pink|purple} eyes,long eyelashes,drooping eyes,{double bun|()}, /* 胸ランダム */, {small|mediun|big} breasts,/* 衣装ランダム */,{bikini|micro bikini|slingshot swimsuit|(china dress, long dress,tight mini skirt, gold decoration dress, sleeveless, ultra detailed dress,cleavage, cleavage cutout, clothing cutout,put on string pants)|(naked lace frill apron with open chest)|(evening dress, deep slit, cleavage)|(Sneakers,sportswear,Flat cap)|(playboy bunny, pantyhose)|(school_uniform,skirt)},/* 場所ランダム */, {beach|desert island|lobby|street},{full body|cowboy shot},{standing|sitting}"

negative = "(zPDXL,score_4,score_5,score_6,source_pony),(source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),(nsfw,nude,nippless,public hair,revealing clothes,bed,on bed,bed room,private parts,take off clothes)"