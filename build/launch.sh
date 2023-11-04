
mkdir -p build/torch
docker run -it --rm \
    -v $(pwd)/build/torch:/root/dev/pytorch/docs/build/torch \
    -v $(pwd)/build/vision:/root/dev/vision/docs/build/vision \
    --gpus all \
    -e NVIDIA_DRIVER_CAPABILITIES=graphics,display,compute,utility \
    -w /root/dev/pytorch/docs/ \
    unknownue/pytorch.docs \
    bash

# pip3 install -r requirements.txt --no-cache-dir
# make html

