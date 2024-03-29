# hash:sha256:982eff2760c6d1aaa06b0ec7470fcb12814202d7b4595a41f5f67500199b1665
FROM registry.codeocean.com/codeocean/miniconda3:4.9.2-python3.8-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils=2.0.6 \
        libasound2-dev=1.2.2-2.1ubuntu2.5 \
        pkg-config=0.29.1-0ubuntu4 \
        python3-dev=3.8.2-0ubuntu2 \
        python3-opencv=4.2.0+dfsg-5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U --no-cache-dir \
    mediapipe==0.8.9.1 \
    musicalbeeps==0.2.9 \
    numpy==1.22.2 \
    opencv-python==4.5.5.64 \
    simpleaudio==1.0.4
