
# See also https://scikit-learn.org/dev/developers/contributing.html#documentation

FROM ubuntu:20.04 AS sklearn

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline Numpy Docs"
LABEL python-version="3.8.x"
LABEL license="MIT"

ARG SKLEARN_VERSION=0.23.2

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

ENV PATH "/root/usr/bin:${PATH}"

RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git wget build-essential ca-certificates && \
    apt clean

# Install Python3 and corresponding pip
RUN apt install -y --no-install-recommends python3 python3-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    apt clean && \
    ln -sf python3 /usr/bin/python && ln -sf pip3 /usr/bin/pip && \
    pip3 install --upgrade pip && \
    pip install --no-cache-dir sphinx sphinx-gallery numpydoc matplotlib Pillow pandas \
            scikit-image packaging seaborn pytest && \
    pip install --no-cache-dir scikit-learn==$SKLEARN_VERSION

# install latex
# RUN apt install -y --no-install-recommends latexmk && \
    # apt install -y --no-install-recommends texlive-latex-extra

RUN git clone https://github.com/scikit-learn/scikit-learn.git && cd scikit-learn && \
    git checkout tags/$SKLEARN_VERSION
    # git submodule init && \
    # git submodule update

WORKDIR /root/scikit-learn/doc
CMD ["bash"]

