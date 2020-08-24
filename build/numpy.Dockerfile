
# See also https://numpy.org/devdocs/docs/howto_build_docs.html

FROM ubuntu:18.04 AS numpy-docs-build

LABEL maintainer="unknownue <unknownue@outlook.com>"
LABEL description="An docker environment to build offline Numpy Docs"
LABEL numpy-version="1.18.1"
LABEL python-version="3.6.x"
LABEL license="MIT"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

ENV PATH "/root/usr/bin:${PATH}"

RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git wget build-essential ca-certificates && \
    apt clean

# Install Python 3.6 and corresponding pip
RUN apt install -y --no-install-recommends python3.6 python3-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && \
    apt clean && \
    ln -sf python3.6 /usr/bin/python && ln -sf pip3 /usr/bin/pip && \
    pip3 install --upgrade pip && \
    pip install --no-cache-dir numpy==1.18.1 sphinx==2.4.2 scipy==1.4.1 ipython Matplotlib numpydoc

# install latex
RUN apt install -y --no-install-recommends latexmk && \
    apt install -y --no-install-recommends texlive-latex-extra

RUN git clone https://github.com/numpy/numpy.git && cd numpy && \
    git checkout tags/v1.18.1 && \
    git submodule init && \
    git submodule update

CMD ["bash"]
