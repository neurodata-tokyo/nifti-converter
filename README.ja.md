# NIfTI Converter

[English](README.md)

このツールは、NIfTI形式の画像ファイルをPNG形式の画像ファイル群に変換するコマンドラインアプリケーションです。

## 必要条件

- Python 3.11以上
- [uv](https://docs.astral.sh/uv/)

## インストール

1. このリポジトリをクローンまたはダウンロードします
2. 依存関係をインストールします:

```sh
uv sync
```

## 使い方

### NIfTIからPNGへの変換

```sh
python nii2iseq.py -i <input_file> [-o <output_directory>] [--prefix <prefix>]
```

オプション:
- `-i`, `--input`: NIfTIファイルのパス
- `-o`, `--output`: ファイルを出力するディレクトリ（オプション）
- `--prefix`: 出力ファイル名のプレフィックス（オプション）

出力ディレクトリを指定しない場合、デフォルトで入力ファイル名（拡張子を除く）のディレクトリが使用されます。

### PNGからNIfTIへの変換

```sh
python iseq2nii.py -i <input_directory> [-o <output_file>]
```

オプション:
- `-i`, `--input`: 入力PNGディレクトリのパス
- `-o`, `--output`: ファイルの出力先（オプション）

出力ファイル名を指定しない場合、デフォルトで入力ディレクトリ名に拡張子を付けたものが使用されます。

## 注意事項

- このツールは3次元のNIfTIファイルのみをサポートしています。4次元以上のデータを含むファイルはエラーとなります。
- 各スライスは`<prefix><XXX>.png`という形式で保存されます（XXXは000から始まる3桁の数字）。