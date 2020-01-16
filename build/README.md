# Build Setups

The build setup require 

Build docker image:

```shell
$ docker build -t pytorch-docs-build .
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