ARG VARIANT="focal"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}


RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    clang-format \
    python3-pip \
    software-properties-common

RUN env lang="ja_jp.utf-8" language="ja_jp:ja" lc_all="ja_jp.utf-8"


RUN sudo add-apt-repository ppa:neovim-ppa/stable && \
    sudo apt-get update && \
    sudo apt-get -y install neovim



