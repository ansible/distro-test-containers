FROM opensuse/leap:15.0

RUN zypper --non-interactive --gpg-auto-import-keys refresh --services --force && \
    zypper --non-interactive install --force systemd-sysvinit && \
    zypper --non-interactive install --auto-agree-with-licenses --no-recommends \
    acl \
    apache2 \
    bzip2 \
    curl \
    dbus-1-python3 \
    gcc \
    git \
    glibc-i18ndata \
    glibc-locale \
    iproute2 \
    lsb-release \
    make \
    mariadb \
    openssh \
    postgresql-server \
    python3-cryptography \
    python3-devel \
    python3-httplib2 \
    python3-Jinja2 \
    python3-keyczar \
    python3-lxml \
    python3-mock \
    python3-PyMySQL \
    python3-nose \
    python3-passlib \
    python3-pip \
    python3-psycopg2 \
    python3-PyYAML \
    python3-selinux \
    python3-setuptools \
    python3-virtualenv \
    rpm-build \
    ruby \
    sshpass \
    subversion \
    sudo \
    tar \
    unzip \
    which \
    zip \
    && \
    zypper clean --all

# systemd path differs from rhel
ENV LIBSYSTEMD=/usr/lib/systemd/system
RUN (cd ${LIBSYSTEMD}/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f ${LIBSYSTEMD}/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f ${LIBSYSTEMD}/local-fs.target.wants/*; \
rm -f ${LIBSYSTEMD}/sockets.target.wants/*udev*; \
rm -f ${LIBSYSTEMD}/sockets.target.wants/*initctl*; \
rm -f ${LIBSYSTEMD}/basic.target.wants/*;

# don't create systemd-session for ssh connections
RUN sed -i /pam_systemd/d /etc/pam.d/common-session-pc

RUN mkdir /etc/ansible/
RUN /usr/bin/echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts
VOLUME /sys/fs/cgroup /run /tmp
RUN ssh-keygen -q -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -t ecdsa -N '' -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key && \
    ssh-keygen -m PEM -q -t rsa -N '' -f /root/.ssh/id_rsa && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    for key in /etc/ssh/ssh_host_*_key.pub; do echo "localhost $(cat ${key})" >> /root/.ssh/known_hosts; done
# explicitly enable the service, opensuse default to disabled services
RUN systemctl enable sshd.service
RUN pip install coverage junit-xml
ENV container=docker
CMD ["/sbin/init"]
