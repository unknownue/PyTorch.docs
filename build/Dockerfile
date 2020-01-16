
FROM ubuntu:18.04 AS pytorch-docs-build

LABEL maintainer="unknownue <usami-ssc@protonmail.com>"
LABEL description="An docker environment to build offline PyTorch Docs"
LABEL pytorch-version="1.4.0"
LABEL vision-version="0.5.0"
LABEL python-version="3.7.x"
LABEL license="MIT"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

RUN apt update && apt upgrade -y && apt clean
RUN apt install -y --no-install-recommends git wget p7zip-full build-essential ca-certificates

ENV PATH "/root/usr/bin:${PATH}"

# Install Python 3.7 and corresponding pip
RUN apt install -y --no-install-recommends python3.7 python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.7 get-pip.py
RUN apt clean
RUN ln -sf python3.7 /usr/bin/python && ln -sf pip3 /usr/bin/pip
RUN pip3 install --upgrade pip

WORKDIR /root/dev/

# clone PyTorch and vision Repository
RUN pip3 install setuptools --no-cache-dir
RUN wget https://github.com/pytorch/vision/archive/v0.5.0.zip -O vision.zip && \
    wget https://github.com/pytorch/pytorch/archive/v1.4.0.zip -O torch.zip
RUN 7z x vision.zip && 7z x torch.zip
RUN rm vision.zip && rm torch.zip && mv vision-0.5.0/ vision/ && mv pytorch-1.4.0/ pytorch/
RUN pip3 install torch==1.4.0 torchvision==0.5.0 --no-cache-dir

# install katex globally. See https://github.com/pytorch/pytorch/issues/27705
RUN apt install -y --no-install-recommends nodejs npm
RUN npm install -g katex

# clean up
RUN apt autoremove -y && apt clean
RUN rm /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python

CMD ["bash"]
