# Build Setups

## Pytorch

The build setup require [Docker](https://docker.com/), and the built image has a size of about 2GB.

```shell
# Build docker image
$ docker build -t unknownue/pytorch.docs -f torch.Dockerfile .

# Build docs for pytorch
$ mkdir -p build/torch
$ docker run --rm \
    -v $(pwd)/build/torch:/root/dev/pytorch/docs/build \
    -w /root/dev/pytorch/docs/ \
    unknownue/pytorch.docs \
    pip3 install -r requirements.txt --no-cache-dir && \
    make html

# Build docs for torchvision
$ mkdir -p build/vision
$ docker run --rm \
    -v $(pwd)/build/vision:/root/dev/vision/docs/build \
    -w /root/dev/vision/docs/ \
    unknownue/pytorch.docs \
    pip3 install -r requirements.txt --no-cache-dir && \
    make html
```

Now the documentation can be found in current `build` directory.

Remove docker images if need:

```shell
$ docker rmi unknownue/pytorch.docs
```

## Numpy

Build docker image:

```shell
$ docker build -t unknownue/numpy.docs -f numpy.Dockerfile .
```

Build the documentation:

```shell
$ mkdir build/
$ docker run --rm \
    -v $(pwd)/build:/root/numpy/doc/build \
    -w /root/numpy/doc/ \
    unknownue/numpy.docs \
    make html
```

After the building finish, the documentation can be found in `build` directory.


## Scikit-learn

Build the docker image:

```shell
$ docker build -t unknownue/sklearn.docs -f sklearn.Dockerfile .
```

```shell
$ mkdir build/
$ docker run --rm \
    -v $(pwd)/build:/root/scikit-learn/doc/_build \
    -w /root/scikit-learn/doc/ \
    unknownue/sklearn.docs \
    make html
```

After the building finish, the documentation can be found in `_build/html/stable` directory.


## Matplotlib

Build the docker image:

```shell
$ docker build -t unknownue/matplotlib.docs -f matplotlib.Dockerfile .
```

```shell
$ mkdir build/
$ docker run --rm \
    -v $(pwd)/build:/root/matplotlib/doc/build \
    -w /root/matplotlib/doc/ \
    unknownue/matplotlib.docs \
    make html
```

After the building finish, the documentation can be found in `build` directory.
