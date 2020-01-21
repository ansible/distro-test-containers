FROM centos:8.1.1911

ENV KEEPLANG="en_US.utf8"

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN dnf clean all && \
    # Remove coreutils-single in favor of coreutils is needed to get the correct
    # version of /usr/bin/sleep
    # Simply running dnf -y --allowerasing install coreutils resulted in a corrupt rpmdb
    rpm -e --nodeps coreutils-single && \
    dnf -y install epel-release && \
    dnf -y --setopt=install_weak_deps=false install \
    acl \
    asciidoc \
    coreutils \
    bzip2 \
    file \
    glibc-langpack-en \
    gcc \
    git \
    iproute \
    libffi \
    libffi-devel \
    libuser \
    make \
    mercurial \
    openssh-clients \
    openssh-server \
    openssl-devel \
    python3-cryptography \
    python3-dbus \
    python3-devel \
    python3-jinja2 \
    python3-lxml \
    python3-nose \
    python3-pip \
    python3-pyyaml \
    python3-setuptools \
    python3-virtualenv \
    rpm-build \
    rubygems \
    sshpass \
    subversion \
    sudo \
    unzip \
    which \
    && \
    dnf clean all && \
    # Cleanup things that take up space
    rm -rf /usr/share/man/* \
        /usr/share/doc/* \
        /usr/share/sgml/* \
        /usr/share/fonts/* \
        /usr/shar/i18n/* && \
    # Remove locales we don't need to save space
    find /usr/lib/locale -mindepth 1 -maxdepth 1 -type d -not \( -name "${KEEPLANG}" -o -name "POSIX" \) -exec rm -rf '{}' +

RUN /usr/bin/sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
RUN mkdir /etc/ansible/
RUN /usr/bin/echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts
VOLUME /sys/fs/cgroup /run /tmp
RUN ssh-keygen -q -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -m PEM -q -t rsa -N '' -f /root/.ssh/id_rsa && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    for key in /etc/ssh/ssh_host_*_key.pub; do echo "localhost $(cat ${key})" >> /root/.ssh/known_hosts; done
RUN pip3 install coverage junit-xml
ENV container=docker
CMD ["/usr/sbin/init"]
