
# See also https://scikit-learn.org/dev/developers/contributing.html#documentation

FROM ubuntu:22.04 AS sklearn

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline scikit-learn Docs"
LABEL license="MIT"

ARG PYTHON_VERSION=3.11
ARG SKLEARN_VERSION=1.3.2

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

ENV PATH "/root/usr/bin:${PATH}"

RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git wget build-essential p7zip-full ca-certificates ffmpeg && \
    apt clean

# Install Python 3 and corresponding pip
RUN apt install -y --no-install-recommends python$PYTHON_VERSION python3-distutils python3-scipy python$PYTHON_VERSION-dev && \
    wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    apt clean && \
    ln -sf python$PYTHON_VERSION /usr/bin/python && ln -sf pip3 /usr/bin/pip
    
RUN pip3 install --upgrade pip && \
	pip3 install pqi && pqi use aliyun

RUN pip3 install --no-cache-dir Cython joblib pytest && \
	pip3 install --no-cache-dir sphinx sphinx-gallery numpydoc matplotlib Pillow pandas \
            scikit-image packaging seaborn sphinx-prompt \
            sphinxext-opengraph sphinx-copybutton plotly pooch && \
    pip install --no-cache-dir scikit-learn==$SKLEARN_VERSION

# install latex
# RUN apt install -y --no-install-recommends latexmk && \
    # apt install -y --no-install-recommends texlive-latex-extra

RUN wget https://github.com/scikit-learn/scikit-learn/archive/refs/tags/$SKLEARN_VERSION.zip -O sklearn.zip && \
	7z x sklearn.zip && rm sklearn.zip && mv scikit-learn-$SKLEARN_VERSION/ sklearn/

WORKDIR /root/scikit-learn/doc
CMD ["bash"]

