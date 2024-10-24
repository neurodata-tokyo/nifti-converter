from enum import Enum
import os
from typing import Annotated
import typer
import nibabel as nib
import numpy as np
from PIL import Image

app = typer.Typer()


@app.command()
def convert_images_to_nifti(
    input_dir: Annotated[
        str, typer.Option("--input", "-i", help="Path to images directory")
    ],
    output_file: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-o",
            help="Output destination for NIfTI file (default is input folder name + '.nii')",
        ),
    ] = None,
):
    # Images to NIfTI conversion process
    image_files = sorted([f for f in os.listdir(input_dir)])
    slices = []
    for image_file in image_files:
        img = Image.open(os.path.join(input_dir, image_file))
        slice_data = np.array(img)
        slices.append(slice_data)
    nifti_data = np.stack(slices, axis=-1)
    affine = np.eye(4)  # Dummy affine matrix, modify as needed
    nifti_img = nib.Nifti1Image(nifti_data, affine)  # type: ignore
    nifti_filename = output_file or (os.path.basename(input_dir) + ".nii")

    nib.save(nifti_img, nifti_filename)  # type: ignore
    typer.echo(f"Saved {nifti_filename}.")


if __name__ == "__main__":
    app()
