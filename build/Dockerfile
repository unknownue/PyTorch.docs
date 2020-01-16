
FROM ubuntu:18.04 AS pytorch-docs-build

LABEL maintainer="unknownue <usami-ssc@protonmail.com>"
LABEL description="An docker environment to build offline PyTorch Docs"
LABEL pytorch-version="1.4.0"
LABEL python-version="3.7.x"
LABEL license="MIT"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

RUN apt update && apt upgrade -y && apt clean
RUN apt install -y --no-install-recommends git wget build-essential ca-certificates

ENV PATH "/root/usr/bin:${PATH}"

# Install Python 3.7 and corresponding pip
RUN apt install -y --no-install-recommends python3.7 python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.7 get-pip.py
RUN apt clean
RUN ln -sf python3.7 /usr/bin/python && ln -sf pip3 /usr/bin/pip
RUN pip3 install --upgrade pip

WORKDIR /root/dev/

# clone PyTorch Repository
RUN pip3 install setuptools --no-cache-dir
RUN git clone https://github.com/pytorch/pytorch.git
RUN pip3 install torch==1.4.0 torchvision==0.5.0 --no-cache-dir

# install sphinx dependencies
RUN rm /usr/bin/python
WORKDIR /root/dev/pytorch
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
WORKDIR /root/dev/pytorch/docs

# install katex globally. See https://github.com/pytorch/pytorch/issues/27705
RUN apt install -y --no-install-recommends nodejs npm
RUN npm install -g katex

# clean up
RUN apt autoremove -y && apt clean
RUN rm /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python

CMD ["bash"]
