
# See also https://github.com/matplotlib/matplotlib/blob/master/doc/devel/documenting_mpl.rst

FROM ubuntu:20.04 AS matplotlib

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline Matplotlib docs"
LABEL python-version="3.8.x"
LABEL license="MIT"

ARG MATPLOTLIB_VERSION=v3.3.1
ARG PYTHON_VERSION=3.8

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/
ENV PATH "/root/usr/bin:${PATH}"

# ADD sources.list /etc/apt/sources.list
RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git wget build-essential ca-certificates && \
    apt clean

RUN apt install -y --no-install-recommends python$PYTHON_VERSION python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py && python$PYTHON_VERSION get-pip.py && \
    ln -sf python$PYTHON_VERSION /usr/bin/python && ln -sf pip3 /usr/bin/pip

RUN pip3 install --upgrade pip
# RUN pip3 install pqi && pqi use aliyun

# Install docs build dependencies
RUN apt install -y --no-install-recommends graphviz python3-tk optipng inkscape && \
    pip install --no-cache-dir matplotlib \
        sphinx sphinx_gallery sphinx_copybutton sphinxcontrib-svg2pdfconverter \
        numpydoc ipython colorspacious scipy ipykernel
# Install latex dependencies
RUN apt install -y --no-install-recommends latexmk && \
    apt install -y --no-install-recommends dvipng texlive-latex-extra cm-super
# RUN apt install -y --no-install-recommends nodejs npm
# RUN npm set registry https://registry.npm.taobao.org/ && \
#     npm install -g katex

RUN git clone https://github.com/matplotlib/matplotlib.git && \
    git checkout tags/$MATPLOTLIB_VERSION

WORKDIR /root/matplotlib/doc
CMD ["bash"]
