from setuptools import setup, find_packages

setup(
    name='sg_shadownet',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'scikit-image==0.15.0',
        'numpy==1.17.4',
        'PyYAML==5.3.1',
        'imageio==2.6.1',
        'matplotlib==3.1.1',
        'Pillow==6.2.1'
    ],
    include_package_data=True,
    description='PyTorch implementation of Style-Guided Shadow Removal',
    author='',
    license='MIT',
)