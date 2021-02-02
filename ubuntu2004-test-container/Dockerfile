FROM quay.io/bedrock/ubuntu:focal-20200423

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    acl \
    apache2 \
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
    python3-nose \
    python3-packaging \
    python3-passlib \
    python3-pip \
    python3-setuptools \
    python3-venv \
    python3-virtualenv \
    python3-wheel \
    python3-yaml \
    reprepro \
    rsync \
    ruby \
    sshpass \
    subversion \
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
RUN mkdir /etc/ansible/
RUN /bin/echo -e "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts
RUN locale-gen en_US.UTF-8
VOLUME /sys/fs/cgroup /run/lock /run /tmp
RUN pip3 install 'coverage==4.5.4' 'resolvelib==0.5.4' 'junit-xml==1.9'
ENV container=docker
CMD ["/sbin/init"]
