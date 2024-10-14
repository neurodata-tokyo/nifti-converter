import os
import typer
import nibabel as nib
import numpy as np
from PIL import Image

app = typer.Typer()


@app.command()
def convert_nifti_to_png(
    input_file: str = typer.Option(
        ..., "--input", "-i", help="入力NIfTIファイルのパス"
    ),
    output_dir: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="ファイルを出力するディレクトリ（デフォルトは入力ファイル名から拡張子を除いたもの）",
    ),
    prefix: str = typer.Option(
        "",
        "--prefix",
        help="出力PNGファイル名のプレフィックス（デフォルトは''）",
    ),
):
    # NIfTIからPNGへの変換処理
    # NIfTIファイルを読み込む
    img = nib.load(input_file)  # type: ignore
    data = img.get_fdata()  # type: ignore

    # データの次元数をチェック
    if data.ndim != 3:
        raise ValueError(
            "サポートされていないデータ形式です。3次元のNIfTIファイルのみ使用可能です。"
        )

    # 出力フォルダが指定されていない場合、入力ファイル名（拡張子なし）のディレクトリを使用
    if output_dir is None:
        output_dir = os.path.splitext(os.path.basename(input_file))[0]

    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    # 各スライスをPNGとして保存
    max_value = data.max()
    min_value = data.min()
    for i in range(data.shape[2]):
        slice_data = data[:, :, i]

        # データを0-255の範囲に正規化
        slice_data = ((slice_data - min_value) / (max_value - min_value) * 255).astype(
            np.uint8
        )

        # PILを使用してPNG画像として保存
        img = Image.fromarray(slice_data)
        img.save(os.path.join(output_dir, f"{prefix}{i:03d}.png"))

    typer.echo(f"{input_file}を{output_dir}にPNGファイルとして保存しました。")


if __name__ == "__main__":
    app()
