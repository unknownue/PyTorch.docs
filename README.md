# PyTorch Offline Documentation

Offline documentation built from official [Scikit-learn](https://github.com/scikit-learn/scikit-learn), [Matplotlib](https://github.com/matplotlib/matplotlib), [PyTorch](https://github.com/pytorch/pytorch.git) and [torchvision](https://github.com/pytorch/vision.git) release.

The offline documentation of [NumPy](https://numpy.org) is available on official website.

Offline documentation does speed up page loading, especially for some countries/regions.

This repo helps to relieve the pain of building PyTorch offline documentation.

No need to clone the huge PyTorch repo. No need to install Sphinx. No need to wait for searching.

| Docs         | Version                                                      | Release Page                                                 |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| PyTorch      | [![torch version](https://img.shields.io/badge/torch_version-v2.1.0-282828.svg?labelColor=4F4F4F&logo=PyTorch)](https://pytorch.org/blog/pytorch-2-1/) | [Link](https://github.com/unknownue/PyTorch.docs/releases/tag/v2.1.0) |
| torchvision  | [![torchvision version](https://img.shields.io/badge/torchvision_version-v0.16.0-282828.svg?labelColor=4F4F4FF&logo=PyTorch)](https://github.com/pytorch/vision/releases/tag/v0.16.0) | [Link](https://github.com/unknownue/PyTorch.docs/releases/tag/v1.11.0) |
| Numpy        | [![numpy version](https://badgen.net/badge/NumPy%20version/v1.26.0/black?icon=dockbit)](https://numpy.org/doc/1.26/release.html) | [Link](https://numpy.org/doc/1.26/numpy-html.zip)                                |
| Scikit-learn | [![scikit-learn version](https://badgen.net/badge/Scikit-learn%20version/v0.22/black?icon=libraries)](https://github.com/scikit-learn/scikit-learn/releases/tag/0.23.2) | [Link](https://github.com/unknownue/PyTorch.docs/releases/tag/v1.7.1) |
| Matplotlib   | [![matplotlib version](https://badgen.net/badge/Matplotlib%20version/v3.3.1/black?icon=graphql)](https://github.com/matplotlib/matplotlib/releases/tag/v3.3.1) | [Link](https://github.com/unknownue/PyTorch.docs/releases/tag/v1.6.1) |

## How to use

You can download from [release page](https://github.com/unknownue/PyTorch.docs/releases)(recommended), or clone this repo(about 700+MB) by

```shell
$ git clone https://github.com/unknownue/PyTorch.docs.git
```

The documentation of PyTorch is in `torch` directory, and that of torchvision is in `torchvision` directory.

Open `Index.html` to view the documentation.

If you want to build by yourself, the `build` directory contains the build configuration in docker.
