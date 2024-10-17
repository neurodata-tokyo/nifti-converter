from enum import Enum
import os
from typing import Annotated
import typer
import nibabel as nib
import numpy as np
from PIL import Image

app = typer.Typer()


class ImageFormat(str, Enum):
    png = "png"
    tiff = "tiff"


@app.command()
def convert_nifti_to_images(
    input_file: Annotated[
        str, typer.Option("--input", "-i", help="Path to the input NIfTI file")
    ],
    output_dir: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-o",
            help="Directory to output files (default is input filename without extension)",
        ),
    ] = None,
    format: Annotated[
        ImageFormat,
        typer.Option(
            "--format",
            "-f",
            help="Image format (default is png)",
        ),
    ] = ImageFormat.png,
    prefix: Annotated[
        str,
        typer.Option(
            "--prefix", help="Prefix for output PNG filenames (default is '')"
        ),
    ] = "",
):
    # NIfTI to PNG conversion process
    # Load NIfTI file
    img = nib.load(input_file)  # type: ignore
    data = img.get_fdata()  # type: ignore

    # Check the number of dimensions in the data
    if data.ndim != 3:
        raise ValueError("Unsupported data format. Only 3D NIfTI files are supported.")

    # If no output folder is specified, use the input filename (without extension) as the directory
    if output_dir is None:
        output_dir = os.path.splitext(os.path.basename(input_file))[0]

    # Create the output folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save each slice as PNG
    max_value = data.max()
    min_value = data.min()
    for i in range(data.shape[2]):
        slice_data = data[:, :, i]

        # Normalize data to 0-255 range
        slice_data = ((slice_data - min_value) / (max_value - min_value) * 255).astype(
            np.uint8
        )

        # Save as PNG image using PIL
        img = Image.fromarray(slice_data)
        img.save(
            os.path.join(output_dir, f"{prefix}{i:03d}.{format.value}"),
            format=format.value,
        )

    typer.echo(f"Saved {input_file} as PNG files in {output_dir}.")


if __name__ == "__main__":
    app()
