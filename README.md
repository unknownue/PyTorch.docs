# PyTorch Offline Documentation

[![numpy version](https://badgen.net/badge/NumPy%20version/v1.8.1/black?icon=dockbit)](https://github.com/numpy/numpy)
[![torch version](https://img.shields.io/badge/torch_version-v1.4.0-g.svg?logo=PyTorch)](https://github.com/pytorch/pytorch)
[![torchvision version](https://img.shields.io/badge/torchvision_version-v0.5.0-g.svg?logo=PyTorch)](https://github.com/pytorch/vision)
[![PyTorch 1.4](https://img.shields.io/badge/PyTorch_1.4-Release_Note-blue.svg?logo=PyTorch)](https://pytorch.org/blog/pytorch-1-dot-4-released-and-domain-libraries-updated/)

Offline documentation built from official [numpy](https://github.com/numpy/numpy.git), [PyTorch](https://github.com/pytorch/pytorch.git) and [torchvision](https://github.com/pytorch/vision.git) release. The documentations of pytorch and torchvision are separate.

Offline documentation does speed up page loading, especially for some countries/regions.

This repo helps to relieve the pain of building PyTorch offline documentation.

No need to clone the huge PyTorch repo. No need to install Sphinx. No need to wait for searching.

## How to use

You can download from [release page](https://github.com/unknownue/docs.PyTorch/releases)(recommended), or clone this repo by

```shell
$ git clone https://github.com/unknownue/docs.PyTorch.git
```

The documentation of PyTorch is in `torch` directory, and that of torchvision is in `torchvision` directory. 

Open `Index.html` to view the documentation.

If you want to build by yourself, the `build` directory contains the build configuration in docker.