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

[Stable Diffusionの新モデル『SDXL』の使い方！導入方法も紹介](https://romptn.com/article/9688)

* Stable Diffusion XL(高解像度画像生成AI)使用方法になります。

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
vi vae_check.py
vi model_check.py

url = "http://IPアドレス:7860"
→上記のIPアドレスを変更する。
```

### 利用モデル確認

以下のコマンドを入力し、モデル情報,VAE情報を確認する。

```bash
python3 model_check.py
cat output/sd_model.txt
→使用するモデルの行を控える。

python3 vae_check.py
cat sd_vae.txt
→使用するvaeの行を控える
```

### 画像生成プログラム準備

以下のコマンドを入力し、準備を行う。

```bash
vi script_SD/base.py
vi script_SDXL/base.py
→StableDiffusion(SD)用、StableDiffusionXL(SDXL)用でそれぞれ編集する。

url = "http://IPアドレス:7860"
→IPアドレスはStableDiffusionが動いているPCのIPを指定すること。

vae = "vae名(前項で調べた対象VAE名)"
→使用するVAE名を控える。

model = "モデル名(前項で調べた対象モデル名)"
modelname = "モデル名(ファイル名に記載する適当なモデル名)"
→前の手順で控えたモデル名を貼り付ける。

script = "/* ベースライン */, (score_9, score_8_up, score_7_up, BREAK source_anime, rating_explicit), (best quality, masterpiece, uncensored, high quality, ultra detailed, extremely detailed CG,beautiful face, beautiful eyes, beautiful hair, kawaii), /* ソロ */, (1girl,solo), /* random girl */,{blue|yellow|red|black|pink|purple} hair,{long|short} hair,straight hair,{blue|yerrow|red|black|pink|purple} eyes,long eyelashes,drooping eyes,{double bun|()}, /* 胸ランダム */, {small|mediun|big} breasts,/* 衣装ランダム */,{bikini|micro bikini|slingshot swimsuit|(china dress, long dress,tight mini skirt, gold decoration dress, sleeveless, ultra detailed dress,cleavage, cleavage cutout, clothing cutout,put on string pants)|(naked lace frill apron with open chest)|(evening dress, deep slit, cleavage)|(Sneakers,sportswear,Flat cap)|(playboy bunny, pantyhose)|(school_uniform,skirt)},/* 場所ランダム */, {beach|desert island|lobby|street},{full body|cowboy shot},{standing|sitting}"

negative = "(zPDXL,score_4,score_5,score_6,source_pony),(source_furry,source_cartoon,lowres,bad anatomy,bad hands,censored,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,artist name,messy color,deformed fingers,bad,distracted,hyper realistic),(nsfw,nude,nippless,public hair,revealing clothes,bed,on bed,bed room,private parts,take off clothes),asuna \(blue archive\), blue archive"

→必要に応じ、上記生成パラメータを変更する。

上記以外にパラメータはあるが必要に応じ、変更してください。
```

### 画像生成プログラム稼働

以下のコマンドを入力し、画像生成する。

```bash
python3 script_SD/create_girl.py (出力したい画像枚数)
python3 script_SDXL/create_girl.py (出力したい画像枚数)

指定しない場合1枚出力されます。

ls output/yyyy-mm-dd/
→画像ファイルが出力されていることを確認する。
```

## 絵の構図を変えずに細かい状態を変えたい場合

画像生成してくると、絵の構図を変えずに服装など変えたくなる場合、
seed値を取得したくなるかと思いますが、簡単な方法として
ブラウザで<https://ローカルIP:7860>に移動して生成AI
Web画面から確認できます。

ただし、PNGファイルでのみ可能。

[Stable DiffusionでSeedの使い方について分かりやすく解説！](https://ai-illust-kouryaku.com/?p=4000#index_id1)

## PNGからjpgへの変換

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
