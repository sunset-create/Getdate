# 選択したフォルダ内にあるjpgのExifデータを持っていれば撮影日、Exifデータを持っていなければ更新日のフォルダを作成して次々に移動
# HEIC、png、avi、mp4も処理。Exifデータで処理されなかったjpgも仕分け
# Rename機能を削除


from PIL import Image
from PIL.ExifTags import TAGS
import glob, os, time, shutil
from tkinter import filedialog

# ダイアログを開き作業ディレクトリを選択
dir = "C:/Users/harry/PycharmProjects"
fld = filedialog.askdirectory(initialdir = dir)
os.chdir(fld)

# ファイルの一覧を列挙 --- (*1)
files = glob.glob("*.jpg")
# 作業フォルダのpathを表示
path=os.getcwd()
print(path)

def file_sort(files):
    for i, photo_name in enumerate(files):
    # ファイルの更新日時を得る --- (*3)
        t = os.path.getmtime(photo_name)
        ts = time.strftime("%Y%m%d", time.localtime(t))
        For_fn = time.strftime("%Y%m%d"'_'"%H%M%S", time.localtime(t))
        r, e = os.path.splitext(photo_name)
    # 更新日時のディレクトリを作成 --- (*4)
        os.makedirs(ts, exist_ok=True)
    # 作成したディレクトリへ写真ファイルを移動 --- (*5)
        new_name = For_fn + e
        shutil.move(photo_name,ts)
        print(ts)

# 繰り返しディレクトリ作成⇒ファイル移動 --- (*2)
for i, photo_name in enumerate(files):

# 画像ファイルを開く
    img = Image.open(photo_name)

    img_exif = img.getexif()

    img.close()

# ファイルがExif情報を持っている場合
    if img_exif:
        # 一覧で表示
        for id, value in img_exif.items():
            if TAGS.get(id, id) == "DateTimeOriginal":
                print(value)
                da = value[0:4]
                db = value[5:7]
                dc = value[8:10]
                dd = value[11:13]
                de = value[14:16]
                df = value[17:19]
                dg = da + db + dc
                dh = da + db + dc + '_' + dd + de + df

                r, e = os.path.splitext(photo_name)
                # 更新日時のディレクトリを作成 --- (*4)
                os.makedirs(dg, exist_ok=True)
                # 作成したディレクトリへ写真ファイルを移動 --- (*5)
                new_name = dh + e

                shutil.move(photo_name, dg)
                print(dg)

# ファイルがexif情報を持っていない場合
    else:
        print("Sorry, image has no exif data.")
        # ファイルの更新日時を得る --- (*3)
        t = os.path.getmtime(photo_name)
        ts = time.strftime("%Y%m%d", time.localtime(t))
        For_fn = time.strftime("%Y%m%d"'_'"%H%M%S", time.localtime(t))
        r, e = os.path.splitext(photo_name)
        # 更新日時のディレクトリを作成 --- (*4)
        os.makedirs(ts, exist_ok=True)
        # 作成したディレクトリへ写真ファイルを移動 --- (*5)
        new_name = For_fn + e
        shutil.move(photo_name, ts)
        print(ts)


# HEICを処理
files = glob.glob("*.HEIC")
file_sort(files)

# pngを処理
files = glob.glob("*.png")
file_sort(files)

# 残ったjpgを処理
files = glob.glob("*.jpg")
file_sort(files)

# mp4を処理
files = glob.glob("*.mp4")
file_sort(files)

# aviを処理
files = glob.glob("*.avi")
file_sort(files)

# movを処理
files = glob.glob("*.mov")
file_sort(files)