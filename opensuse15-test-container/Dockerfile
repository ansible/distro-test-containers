FROM quay.io/bedrock/leap:15.2

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
    openssh \
    postgresql-server \
    python3-cairo \
    python3-cryptography \
    python3-devel \
    python3-httplib2 \
    python3-Jinja2 \
    python3-lxml \
    python3-mock \
    python3-nose \
    python3-packaging \
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
RUN ssh-keygen -A
# explicitly enable the service, opensuse default to disabled services
RUN systemctl enable sshd.service
RUN pip install 'coverage==4.5.4' 'resolvelib==0.5.4' 'junit-xml==1.9'
# 15.2 ships with a broken ensurepip, we need to replace this .whl
ADD https://ansible-ci-files.s3.amazonaws.com/distro-test-container-files/setuptools-44.1.1-py2.py3-none-any.whl \
  /usr/lib64/python3.6/ensurepip/_bundled/setuptools-44.1.1-py2.py3-none-any.whl
ENV container=docker
CMD ["/sbin/init"]
