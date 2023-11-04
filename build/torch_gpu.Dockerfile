
FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04 AS pytorch-docs-build

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline PyTorch Docs"
LABEL license="MIT"

ENV DEBIAN_FRONTEND=noninteractive

ARG VERSION_PYTHON=python3.11
ARG VERSION_PYTORCH=2.1.0
ARG VERSION_VISION=0.16.0

WORKDIR /root/
ADD ubuntu-mirror-2204.txt /etc/apt/sources.list

RUN apt update && apt install -y ca-certificates
RUN apt update && \
    apt install -y --no-install-recommends git wget p7zip-full build-essential && \
    apt install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt clean

# ENV PATH "/root/usr/bin:${PATH}"

# Install Python and corresponding pip
RUN apt install -y --no-install-recommends $VERSION_PYTHON python3-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && $VERSION_PYTHON get-pip.py && \
    # $VERSION_PYTHON get-pip.py && \
    apt install -y --no-install-recommends $VERSION_PYTHON-dev && \
    apt clean && \
    ln -sf $VERSION_PYTHON /usr/bin/python && ln -sf pip3 /usr/bin/pip
# RUN pip3 install pqi && pqi use aliyun

WORKDIR /root/dev/

# clone PyTorch and vision Repository
RUN pip3 install setuptools --no-cache-dir && \
    wget https://github.com/pytorch/vision/archive/v$VERSION_VISION.zip -O vision.zip && \
    wget https://github.com/pytorch/pytorch/archive/v$VERSION_PYTORCH.zip -O torch.zip && \
    7z x vision.zip && 7z x torch.zip && \
    rm vision.zip && rm torch.zip && mv vision-$VERSION_VISION/ vision/ && mv pytorch-$VERSION_PYTORCH/ pytorch/

RUN wget https://download.pytorch.org/whl/cu121/torch-2.1.0%2Bcu121-cp311-cp311-linux_x86_64.whl && \
	wget https://download.pytorch.org/whl/cu121/torchvision-0.16.0%2Bcu121-cp311-cp311-linux_x86_64.whl && \
	pip3 install torch-2.1.0+cu121-cp311-cp311-linux_x86_64.whl && \
	pip3 install torchvision-0.16.0+cu121-cp311-cp311-linux_x86_64.whl && \
	rm torch-2.1.0+cu121-cp311-cp311-linux_x86_64.whl && \
	rm torchvision-0.16.0+cu121-cp311-cp311-linux_x86_64.whl

RUN wget https://raw.githubusercontent.com/pytorch/pytorch/v$VERSION_PYTORCH/requirements.txt -P /home/unknownue/deps/ && \
    echo "torch==$VERSION_PYTORCH" >> /home/unknownue/deps/requirements.txt && \
    echo "torchvision==$VERSION_VISION" >> /home/unknownue/deps/requirements.txt && \
    pip3 install --no-cache-dir --no-deps -r /home/unknownue/deps/requirements.txt
#    pip3 install torch==$VERSION_PYTORCH torchvision==$VERSION_VISION --no-cache-dir

# install katex globally. See https://github.com/pytorch/pytorch/issues/27705
RUN apt install -y --no-install-recommends nodejs npm
RUN npm cache clear --force && \
	npm config set registry https://registry.npmmirror.com && \
    npm install -g katex

# clean up
RUN apt autoremove -y && apt clean && \
    rm /usr/bin/python && ln -s /usr/bin/$VERSION_PYTHON /usr/bin/python

CMD ["bash"]

