#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# conda install pillow
import os, glob
from PIL import Image

def Main():
    filepath_list = glob.glob(input_path + '/*.png') # .pngファイルをリストで取得する
    for filepath in filepath_list:
        basename  = os.path.basename(filepath) # ファイルパスからファイル名を取得
        save_filepath = out_path + '/' + basename [:-4] + '.jpg' # 保存ファイルパスを作成
        img = Image.open(filepath)
        img = img.convert('RGB') # RGBA(png)→RGB(jpg)へ変換
        img.save(save_filepath, "JPEG", quality=95)
        print(filepath, '->', save_filepath)
        if flag_delete_original_files:
            os.remove(filepath)
            print('delete', filepath)

if __name__ == '__main__':
    input_path = './output/png' # オリジナルpngファイルがあるフォルダを指定
    out_path = './output/jpg' # 変換先のフォルダを指定
    flag_delete_original_files = True # 元ファイルを削除する場合は、True指定

    Main()