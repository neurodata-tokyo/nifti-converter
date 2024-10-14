import os
import typer
import nibabel as nib
import numpy as np
from PIL import Image

app = typer.Typer()


@app.command()
def convert_png_to_nifti(
    input_dir: str = typer.Option(..., "--input", "-i", help="PNGディレクトリのパス"),
    output_file: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="NIfTIファイルの出力先（デフォルトは入力フォルダ名+'.nii'）",
    ),
):
    # PNGからNIfTIへの変換処理
    png_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".png")])
    slices = []
    for png_file in png_files:
        img = Image.open(os.path.join(input_dir, png_file))
        slice_data = np.array(img)
        slices.append(slice_data)
    nifti_data = np.stack(slices, axis=-1)
    affine = np.eye(4)  # 仮のアフィンマトリックス、必要に応じて変更してください
    nifti_img = nib.Nifti1Image(nifti_data, affine)  # type: ignore
    nifti_filename = output_file or (os.path.basename(input_dir) + ".nii")

    nib.save(nifti_img, nifti_filename)  # type: ignore
    typer.echo(f"{nifti_filename} を保存しました。")


if __name__ == "__main__":
    app()
