FROM fedora:30

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*;

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
    mariadb-server \
    # OpenSSH 8.0 generates PEM keys in PKCS8 format, which Paramiko does not recognize
    # https://bugzilla.redhat.com/show_bug.cgi?id=1722285
    # https://github.com/paramiko/paramiko/issues/1015
    openssh-clients-7.9p1 \
    openssh-server-7.9p1 \
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
    python3-mysql \
    python3-nose \
    python3-passlib \
    python3-pip \
    python3-PyYAML \
    python3-setuptools \
    python3-virtualenv \
    rpm-build \
    rubygems \
    rubygem-rdoc \
    sshpass \
    subversion \
    sudo \
    tar \
    unzip \
    which \
    zip \
    && \
    dnf clean all

RUN localedef --quiet -c -i en_US -f UTF-8 en_US.UTF-8
RUN /usr/bin/sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
RUN mkdir /etc/ansible/
RUN /usr/bin/echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts
VOLUME /sys/fs/cgroup /run /tmp
RUN ssh-keygen -q -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -m PEM -q -t rsa -N '' -f /root/.ssh/id_rsa && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    for key in /etc/ssh/ssh_host_*_key.pub; do echo "localhost $(cat ${key})" >> /root/.ssh/known_hosts; done
# Update to the latest version of OpenSSH once the key is generated
RUN dnf -y update \
    openssh-clients \
    openssh-server \
    && \
    dnf clean all
RUN pip3 install coverage junit-xml
ENV container=docker
CMD ["/usr/sbin/init"]
