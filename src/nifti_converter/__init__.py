"""
NIfTI Converter
"""

# Library
from .nii2iseq import convert_nifti_to_images
from .iseq2nii import convert_images_to_nifti

# CLI
from .nii2iseq import app as nii2iseq_app
from .iseq2nii import app as iseq2nii_app

__all__ = [
    "convert_nifti_to_images",
    "convert_images_to_nifti",
    "nii2iseq_app",
    "iseq2nii_app",
]
