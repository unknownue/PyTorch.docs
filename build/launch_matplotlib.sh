
mkdir -p build/matplotlib
docker run -it --rm \
    -v $(pwd)/build/matplotlib:/root/matplotlib/doc/build \
    -w /root/matplotlib/doc/ \
    unknownue/matplotlib.docs \
    bash

