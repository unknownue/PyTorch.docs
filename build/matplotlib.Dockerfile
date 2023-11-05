
# See also https://github.com/matplotlib/matplotlib/blob/master/doc/devel/documenting_mpl.rst

FROM ubuntu:22.04 AS matplotlib

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline Matplotlib docs"
LABEL license="MIT"

ARG MATPLOTLIB_VERSION=3.8.1
ARG PYTHON_VERSION=3.11

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/
ADD ubuntu-mirror-2204.txt /etc/apt/sources.list
ENV PATH "/root/usr/bin:${PATH}"

# ADD sources.list /etc/apt/sources.list
RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git wget build-essential p7zip-full ca-certificates ffmpeg && \
    apt clean

RUN apt install -y --no-install-recommends python$PYTHON_VERSION python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py && python$PYTHON_VERSION get-pip.py && \
    ln -sf python$PYTHON_VERSION /usr/bin/python && ln -sf pip3 /usr/bin/pip

RUN pip3 install --upgrade pip
RUN pip3 install pqi && pqi use aliyun

# Install docs build dependencies
RUN apt install -y --no-install-recommends graphviz python3-tk optipng inkscape && \
    pip install --no-cache-dir matplotlib==$MATPLOTLIB_VERSION \
        sphinx sphinx_gallery sphinx_copybutton sphinxcontrib-svg2pdfconverter \
        numpydoc ipython colorspacious scipy ipykernel

# Install latex dependencies
RUN apt install -y --no-install-recommends latexmk && \
    apt install -y --no-install-recommends dvipng texlive-latex-extra texlive-full cm-super && \
    apt install -y --no-install-recommends ttf-mscorefonts-installer fonts-noto-cjk fonts-humor-sans

RUN wget https://github.com/matplotlib/matplotlib/archive/refs/tags/v$MATPLOTLIB_VERSION.zip -O matplotlib.zip && \
	7z x matplotlib.zip && rm matplotlib.zip && mv matplotlib-$MATPLOTLIB_VERSION/ matplotlib/

WORKDIR /root/matplotlib/doc
CMD ["bash"]
