# CreateAI_API

StableDiffusionから画像を入手するプログラムになります。

## 参考URL

[Stable Diffusion (AUTOMATIC1111) をAPIで操作する ～WEB UI不要で任意のサービスと連携～](https://note.com/rcat999/n/n1beb8d75d334#549b1d65-7771-4478-9578-af0377abb956)

## 事前作業

以下のサイトを参考にローカルPCまたはGoogleColabへStableDiffusionを導入する。

[【Stable Diffusion Web UI】Windowsにダウンロード・インストールする方法](https://soroban.highreso.jp/article/article-036)

[【Stable Diffusion Web UI】Macダウンロード・インストールする方法](https://soroban.highreso.jp/article/article-037)

[【Stable Diffusion Web UI】GoogleColabダウンロード・インストールする方法](https://soroban.highreso.jp/article/article-037)

* Proへの加入が必要(月1179円必要になります。)

[Stable Diffusionでアニメ系美少女を作る方法！呪文(プロンプト)やモデルも](https://romptn.com/article/6236)

* RTX3060導入WindowsPCまたはM1mac利用をおすすめします。
* あらかじめここで操作方法の理解をすることをおすすめします。

[【Stable Diffusion】API経由で画像を大量に生成する方法](https://product.plex.co.jp/entry/stable-diffusion-via-api)

* Stable Diffusion web UI を起動するの起動オプションに"--api"をつける。

[ローカルネットワーク上のAUTOMATIC1111に別マシンからアクセスする](https://qiita.com/kume_negitoro/items/2e4f667cf6e0aee9fab4)

* Stable Diffusion web UI を起動するの起動オプションに"--listen"をつける。

## 使用方法

事前作業ができればどこのPCから操作しても問題ありません。

python,requestsを導入しておくこと。

[Pythonのインストール方法](https://www.klv.co.jp/corner/python-opencv-python-install.html)

[【Python】Requestsをインストールする方法](https://pg-chain.com/python-requests-install)

### ソース入手

以下のgitコマンドで入手する。

```bash
git clone https://github.com/naritomo08/CreateAI_API.git
cd CreateAI
rm -rf .git
```

### URL設定

以下のファイルを開き、最初にある以下の行のIPアドレスをStableDiffusionが動いているPCIPに変更する。

```bash
vi create.py
vi model_check.py

url = "http://IPアドレス:7860"
→上記のIPアドレスを変更する。
```

### 利用モデル確認

以下のコマンドを入力し、モデル情報を確認する。

```bash
python3 model_check.py
cat model_check.py
cat output/sd_model.txt
→使用するモデルの行を控える。
```

### 画像生成プログラム準備

以下のコマンドを入力し、準備を行う。

```bash
vi create.py

model = "モデル名"
→前の手順で控えたモデル名を貼り付ける。

Imgsetting = {
	"prompt": "score_9,score_8_up,score_7_up BREAK source_anime,rating_explicit,(best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG, beautiful face, beautiful eyes, beautiful hair, kawaii:1.2),1girl,solo,long hair,green hair,blue eyes,tanned skin,beach,at midnight,arms up behind,kind_smile,portrait,medium breasts,shirt",
	"negative_prompt":"(zPDXL,score_4,score_5,score_6,source_pony,source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),nsfw,nude",
	"steps": 30,
	"sampler_index":"DPM++ 2M Karras",
	"width": 1024,
	"height": 1024,
	"cfg_scale": 7,
	"seed": -1,
	}
→必要に応じ、上記生成パラメータを変更する。
```

### 画像生成プログラム稼働

以下のコマンドを入力し、画像生成する。

```bash
python3 create.py
ls output/yyyy-mm-dd/
→画像ファイルが出力されていることを確認する。
```

## 絵の構図を変えずに細かい状態を変えたい場合

画像生成してくると、絵の構図を変えずに服装など変えたくなる場合、
seed値を取得したくなるかと思いますが、簡単な方法として
ブラウザで"https://ローカルIP:7860"に移動して生成AI
Web画面から確認できます。

ただし、PNGファイルでのみ可能。

[Stable DiffusionでSeedの使い方について分かりやすく解説！](https://ai-illust-kouryaku.com/?p=4000#index_id1)

## PNGからｊｐｇへの変換

PNGだとファイル容量が大きいため、JPEGへ変換したい際は以下の手順で変換できる。

以下のコマンドで必要モジュールを導入する。

```bash
pip3 install pillow
```

変換したいファイルをoutput/pngフォルダへ保管する。

変換を実施すると元ファイルを削除してしまうため注意。

以下のコマンドを入力し変換を行う。

```bash
python3 convert_jpg.py
ls output/jpg
→変換した画像ファイルが出力されていることを確認する。
```

## script lisｔ(参考)

pronpt

```bash
立ち絵、上半身 1024X1024

(score_9,score_8_up,score_7_up BREAK source_anime,rating_explicit),(best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG, beautiful face, beautiful eyes, beautiful hair, kawaii),1girl,long hair,green hair,blue eyes,tanned skin,beach,arms up behind,kind_smile,portrait,medium breasts,black o-ring_bikini

立ち絵、全身 640X1534

(score_9,score_8_up,score_7_up BREAK source_anime,rating_explicit),(best quality, masterpiece, uncensored, high quality, ultra detailed,extremely detailed CG,beautiful face, beautiful eyes, beautiful hair, kawaii),1girl,blue hair,long hair,straight hair,red eyes,longeyelashes,drooping eyes,medium breasts,frontview,full_shot,kind_smile,arms_behind_back,school_uniform
```

negative pronpt

```bash
/* base */,
(zPDXL,score_4,score_5,score_6,source_pony,source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),(nsfw,nude,nippless,public hair,revealing clothes,bed,on bed,bed room,private parts,take off clothes),
```
