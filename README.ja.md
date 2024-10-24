# NIfTI Converter

<!-- PyPIから飛べるように絶対パスを指定 -->
[English](https://github.com/neurodata-tokyo/nifti-converter/blob/main/README.md)

このツールは、NIfTI形式の画像ファイルと一般的な画像ファイル形式（PNG、TIFF等）の間で変換を行うコマンドラインアプリケーションです。

## インストール

```sh
pip install nifti-converter
```

## 使い方

### NIfTIから画像列への変換

```sh
nii2iseq -i <input_file> [-o <output_directory>] [--prefix <prefix>]
```

オプション:
- `-i`, `--input`: NIfTIファイルのパス
- `-o`, `--output`: ファイルを出力するディレクトリ（デフォルト: 入力ファイル名（拡張子を除く）と同名）
- `--prefix`: 出力ファイル名のプレフィックス（デフォルト: ""）
- `-f`, `--format`: 出力ファイルの形式（デフォルト: png）

#### 注意事項

- 3次元のNIfTIファイルのみをサポートしています。4次元以上のデータを含むファイルはエラーとなります。
- 出力ファイルの形式はpngとtiffのみ対応しています。
- 各スライスは`<prefix><XXX>.<format>`という形式で保存されます（XXXは000から始まる3桁の数字）。

### 画像列からNIfTIへの変換

```sh
iseq2nii -i <input_directory> [-o <output_file>]
```

オプション:
- `-i`, `--input`: 入力画像ディレクトリのパス
- `-o`, `--output`: ファイルの出力先（デフォルト: "<入力ディレクトリ名>.nii"）

## 開発者向け

### 前提条件

- [uv](https://docs.astral.sh/uv/)

### インストール

1. このリポジトリをクローンします
2. 依存関係をインストールします:

```sh
cd nifti-converter
uv sync
```

### 動作確認

修正したアプリをローカルで実行するには以下のコマンドを実行します。

```sh
# NIfTIから画像列への変換
uv run nii2iseq -i <input_file> [-o <output_directory>] [--prefix <prefix>]
# 画像列からNIfTIへの変換
uv run iseq2nii -i <input_directory> [-o <output_file>]
```
