FROM quay.io/bedrock/centos:7.9.2009

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum clean all && \
    yum -y install epel-release && \
    yum -y upgrade && \
    yum -y install \
    acl \
    asciidoc \
    bzip2 \
    dbus-python \
    file \
    gcc \
    git \
    iproute \
    libffi \
    libffi-devel \
    make \
    openssh-clients \
    openssh-server \
    openssl-devel \
    python-cryptography \
    python-devel \
    python-httplib2 \
    python-jinja2 \
    python-lxml \
    python-mock \
    python2-packaging \
    python2-passlib \
    python-pip \
    python-setuptools \
    python-virtualenv \
    PyYAML \
    rpm-build \
    rubygems \
    sshpass \
    subversion \
    sudo \
    unzip \
    which \
    && \
    yum clean all && \
    rm -rf /usr/share/fonts/* \
        /usr/share/i18n/* \
        /usr/share/sgml/docbook/xsl-stylesheets* \
        /usr/share/adobe/resources/*

RUN ssh-keygen -A

COPY requirements.txt /usr/share/container-setup/requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir -r /usr/share/container-setup/requirements.txt

ENV container=docker
CMD ["/sbin/init"]
