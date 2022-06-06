FROM quay.io/bedrock/alpine:3.16.0

# Keep this as basic as possible, so we properly test against BusyBox
# Things like tar/zip are needed by unarchive
# diffutils is installed for runme.sh tests that call diff
# coreutils was explicitly omitted
# sshpass was explicitly omitted as BusyBox timeout causes issues with our connection_ssh tests
RUN apk add --no-cache openrc \
        acl \
        apache2 \
        bzip2 \
        curl \
        diffutils \
        file \
        gawk \
        gcc \
        git \
        libffi-dev \
        make \
        openssh-client \
        openssh-server \
        openssh-sftp-server \
        openssl-dev \
        python3 \
        python3-dev \
        py3-nose \
        py3-pip \
        py3-jinja2 \
        py3-cryptography \
        py3-lxml \
        py3-mock \
        py3-packaging \
        py3-setuptools \
        py3-virtualenv \
        py3-yaml \
        py3-wheel \
        ruby \
        rsync \
        subversion \
        sudo \
        tar \
        tzdata \
        unzip \
        zip \
        musl-dev \
        yaml-dev \
        ca-certificates \
        iproute2-minimal \
        py3-passlib \
        pass \
        gnupg

RUN mkdir /etc/ansible/
RUN /bin/echo -e "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts
RUN ssh-keygen -A
RUN rc-update add sshd
# inittab has some tty entries that cause issues
RUN sed -i '/getty/d' /etc/inittab
# The root account is locked by default, this effectively unlocks it
RUN echo root:ansible | chpasswd

VOLUME /sys/fs/cgroup /run/lock /run /tmp

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

ENV container=docker
CMD ["/sbin/init"]
