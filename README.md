# NIfTI Converter

<!-- Specify absolute path to allow navigation from PyPI -->
[日本語](https://github.com/neurodata-tokyo/nifti-converter/blob/main/README.ja.md)

This tool is a command-line application that converts between NIfTI format image files and common image file formats (PNG, TIFF, etc.).

## Installation

```sh
pip install nifti-converter
```

## Usage

### Converting NIfTI to image sequence

```sh
nii2iseq -i <input_file> [-o <output_directory>] [--prefix <prefix>]
```

Options:
- `-i`, `--input`: Path to the NIfTI file
- `-o`, `--output`: Directory to output files (default: same name as input file without extension)
- `--prefix`: Prefix for output file names (default: "")
- `-f`, `--format`: Output file format (default: png)

#### Notes

- This tool only supports 3D NIfTI files. Files containing 4D or higher dimensional data will result in an error.
- Only png and tiff formats are supported for output files.
- Each slice is saved in the format `<prefix><XXX>.<format>` (where XXX is a 3-digit number starting from 000).

### Converting image sequence to NIfTI

```sh
iseq2nii -i <input_directory> [-o <output_file>]
```

Options:
- `-i`, `--input`: Path to the input image directory
- `-o`, `--output`: Output file destination (default: "<input_directory_name>.nii")

## For Developers

### Prerequisites

- [uv](https://docs.astral.sh/uv/)

### Installation

1. Clone this repository
2. Install dependencies:

```sh
cd nifti-converter
uv sync
```

### Testing

To run the modified application locally, execute the following command:

```sh
# Converting NIfTI to image sequence
uv run nii2iseq -i <input_file> [-o <output_directory>] [--prefix <prefix>]
# Converting image sequence to NIfTI
uv run iseq2nii -i <input_directory> [-o <output_file>]
```
