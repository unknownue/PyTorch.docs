
FROM ubuntu:20.04 AS pytorch-docs-build

LABEL maintainer="unknownue <usami-ssc@protonmail.com>"
LABEL description="An docker environment to build offline PyTorch Docs"
LABEL python-version="3.8.x"
LABEL license="MIT"

ENV DEBIAN_FRONTEND=noninteractive

ARG VERSION_PYTORCH=1.7.0
ARG VERSION_VISION=0.8.0

WORKDIR /root/
# ADD sources.list /etc/apt/sources.list

RUN apt update
RUN apt install -y ca-certificates && \
    apt install -y --no-install-recommends git wget p7zip-full build-essential && \
    apt clean

# ENV PATH "/root/usr/bin:${PATH}"

# Install Python 3.8 and corresponding pip
RUN apt install -y --no-install-recommends python3.8 python3-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && python3.8 get-pip.py && \
    # python3.8 get-pip.py && \
    apt clean && \
    ln -sf python3.8 /usr/bin/python && ln -sf pip3 /usr/bin/pip
# RUN pip3 install pqi && pqi use aliyun

WORKDIR /root/dev/

# clone PyTorch and vision Repository
RUN pip3 install setuptools --no-cache-dir && \
    wget https://github.com/pytorch/vision/archive/v$VERSION_VISION.zip -O vision.zip && \
    wget https://github.com/pytorch/pytorch/archive/v$VERSION_PYTORCH.zip -O torch.zip && \
    7z x vision.zip && 7z x torch.zip && \
    rm vision.zip && rm torch.zip && mv vision-$VERSION_VISION/ vision/ && mv pytorch-$VERSION_PYTORCH/ pytorch/ && \
    pip3 install torch==$VERSION_PYTORCH torchvision==$VERSION_VISION --no-cache-dir

# install katex globally. See https://github.com/pytorch/pytorch/issues/27705
RUN apt install -y --no-install-recommends nodejs npm
RUN npm set registry https://registry.npm.taobao.org/ && \
    npm install -g katex

# clean up
RUN apt autoremove -y && apt clean && \
    rm /usr/bin/python && ln -s /usr/bin/python3.8 /usr/bin/python

CMD ["bash"]
