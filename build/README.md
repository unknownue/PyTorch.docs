# Build Setups

The build setup require 

Build docker image:

```shell
$ docker build -t pytorch-docs-build .
```

Run the container:

```shell
$ docker run --rm -it -v $(pwd)/build:/root/dev/pytorch/docs/build -w /root/dev/pytorch/docs pytorch-docs-build
```

In the `pytorch-docs-build` container:

```shell
# list all available build options
$ make
# make pytorch documentation into html files
$ make dirhtml
```

