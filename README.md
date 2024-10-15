# NIfTI Converter

[日本語](README.ja.md)

This tool is a command-line application that converts between NIfTI format image files and common image file formats (PNG, TIFF, etc.).

## Requirements

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/)

## Installation

1. Clone or download this repository
2. Install dependencies:
```sh
uv sync
```

## Usage

### Converting NIfTI to image sequence

```sh
python nii2iseq.py -i <input_file> [-o <output_directory>] [--prefix <prefix>]
```

Options:
- `-i`, `--input`: Path to the NIfTI file
- `-o`, `--output`: Directory to output files (optional)
- `--prefix`: Prefix for output file names (optional)

If no output directory is specified, a directory named after the input file (without extension) will be used by default.

### Converting image sequence to NIfTI

```sh
python iseq2nii.py -i <input_directory> [-o <output_file>]
```

Options:
- `-i`, `--input`: Path to the input image directory
- `-o`, `--output`: Output file destination (optional)

If no output file name is specified, the input directory name with an extension will be used by default.

## Notes

- This tool only supports 3D NIfTI files. Files containing 4D or higher dimensional data will result in an error.
- Each slice is saved in the format `<prefix><XXX>.<format>` (where XXX is a 3-digit number starting from 000).
