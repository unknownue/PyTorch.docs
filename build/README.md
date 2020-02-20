# Build Setups

## Pytorch

The build setup require [Docker](https://docker.com/), and the built image has a size of about 2GB.

Build docker image:

```shell
$ docker build -t pytorch-docs-build -f torch.Dockerfile .
```

Run the container:

```shell
$ mkdir build
$ docker run --rm -it -v $(pwd)/build:/root/dev/build -w /root/dev/ pytorch-docs-build
```

In the `pytorch-docs-build` container:

```shell
$ cd /root/dev/pytorch/docs
$ pip3 install -r requirements.txt --no-cache-dir
# list all available build options
$ make
# make pytorch documentation into html files
$ make html
# After build finish, the documentation pages are available in build/html directory.
$ mv build/html /root/dev/build/torch


# Then go to build torchvision documentation
$ cd /root/dev/vision/docs
$ pip3 install -r requirements.txt --no-cache-dir
$ make html
# After build finish, the documentation pages are available in build/html directory.
$ mv build/html /root/dev/build/vision
# exit container
$ exit
```

Now the documentation can be found in current `build` directory.


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

