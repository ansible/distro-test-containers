FROM quay.io/bedrock/leap:15.2

RUN zypper --non-interactive --gpg-auto-import-keys refresh --services --force && \
    zypper --non-interactive install --force systemd-sysvinit && \
    zypper --non-interactive install --auto-agree-with-licenses --no-recommends \
    acl \
    apache2 \
    bzip2 \
    curl \
    dbus-1-python \
    gcc \
    git \
    glibc-i18ndata \
    glibc-locale \
    iproute2 \
    lsb-release \
    make \
    openssh \
    postgresql-server \
    python2-cairo \
    python-cryptography \
    python-devel \
    python-httplib2 \
    python-jinja2 \
    python-lxml \
    python-mock \
    python-nose \
    python2-packaging \
    python-passlib \
    python-pip \
    python-psycopg2 \
    python-PyYAML \
    python-setuptools \
    python-virtualenv \
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
RUN ssh-keygen -A
# explicitly enable the service, opensuse default to disabled services
RUN systemctl enable sshd.service

COPY requirements.txt /tmp/requirements.txt
RUN pip install --disable-pip-version-check -r /tmp/requirements.txt && rm /tmp/requirements.txt

ENV container=docker
CMD ["/sbin/init"]
