FROM quay.io/fedora/fedora:35

RUN dnf clean all && \
    dnf -y upgrade && \
    dnf -y --allowerasing install coreutils && \
    dnf -y --setopt=install_weak_deps=false install \
    acl \
    bzip2 \
    file \
    findutils \
    gcc \
    git \
    glibc-locale-source \
    iproute \
    libffi \
    libffi-devel \
    make \
    openssh-clients \
    openssh-server \
    openssl-devel \
    pass \
    procps \
    python3-cryptography \
    python3-dbus \
    python3-devel \
    python3-dnf \
    python3-httplib2 \
    python3-jinja2 \
    python3-lxml \
    python3-mock \
    python3-nose \
    python3-packaging \
    python3-passlib \
    python3-pip \
    python3-PyYAML \
    python3-resolvelib \
    python3-setuptools \
    python3-virtualenv \
    rpm-build \
    rubygems \
    rubygem-rdoc \
    sshpass \
    subversion \
    sudo \
    systemd \
    tar \
    unzip \
    which \
    zip \
    && \
    dnf clean all

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    (cd /lib/systemd/system/multi-user.target.wants/; for i in *; do [ $i == systemd-user-sessions.service ] || rm -f $i; done); \
    rm -f /etc/systemd/system/*.wants/*; \
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*; \
    rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN localedef --quiet -c -i en_US -f UTF-8 en_US.UTF-8
RUN /usr/bin/sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
# pam_loginuid wants to write to /proc/self/loginuid on new ssh session, but can't.
# https://github.com/lxc/lxc/issues/661#issuecomment-222444916
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=726661
RUN /usr/bin/sed -i -e '/pam_loginuid\.so$/ s/required/optional/' /etc/pam.d/*
# allow ssh-rsa key authentication, which is required for paramiko and EC2 compatibility
RUN /usr/bin/sed -i -e 's/^PubkeyAcceptedKeyTypes /PubkeyAcceptedKeyTypes ssh-rsa,/' /usr/share/crypto-policies/DEFAULT/openssh.txt
RUN /usr/bin/sed -i -e 's/^PubkeyAcceptedKeyTypes /PubkeyAcceptedKeyTypes ssh-rsa,/' /usr/share/crypto-policies/DEFAULT/opensshserver.txt
VOLUME /sys/fs/cgroup /run /tmp
RUN ssh-keygen -A
RUN systemctl enable sshd.service

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

ENV container=docker
CMD ["/usr/sbin/init"]
