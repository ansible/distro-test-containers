FROM public.ecr.aws/docker/library/ubuntu:jammy-20240911.1

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y --no-install-recommends && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    acl \
    bzip2 \
    curl \
    debhelper \
    debianutils \
    devscripts \
    docbook-xml \
    dpkg-dev \
    fakeroot \
    gawk \
    gcc \
    git \
    iproute2 \
    libffi-dev \
    libssl-dev \
    libxml2-utils \
    locales \
    lsb-release \
    make \
    pass \
    openssh-client \
    openssh-server \
    python3-cryptography \
    python3-dev \
    python3-dbus \
    python3-httplib2 \
    python3-jinja2 \
    python3-lxml \
    python3-mock \
    python3-packaging \
    python3-passlib \
    python3-pip \
    python3-resolvelib \
    python3-setuptools \
    python3-venv \
    python3-virtualenv \
    python3-wheel \
    python3-yaml \
    reprepro \
    rsync \
    sshpass \
    sudo \
    systemd \
    tzdata \
    unzip \
    virtualenv \
    xsltproc \
    zip \
    && \
    apt-get clean \
    && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /lib/systemd/systemd /sbin/init
RUN rm /etc/apt/apt.conf.d/docker-clean
RUN locale-gen en_US.UTF-8

COPY requirements.txt /usr/share/container-setup/requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir -r /usr/share/container-setup/requirements.txt

ENV container=docker
CMD ["/sbin/init"]
