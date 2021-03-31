FROM quay.io/bedrock/centos:6.10

COPY centos610-vault.repo /etc/yum.repos.d/centos610-vault.repo

RUN rm /etc/yum.repos.d/CentOS-Base.repo && \
    yum clean all && \
    yum -y install epel-release && \
    yum -y install \
    acl \
    asciidoc \
    bzip2 \
    file \
    gcc \
    git \
    libffi \
    libffi-devel \
    make \
    openssh-clients \
    openssh-server \
    openssl-devel \
    python-argparse \
    python-devel \
    python-httplib2 \
    python-jinja2 \
    python-lxml \
    python-mock \
    python-nose \
    python-passlib \
    python-pip \
    python-setuptools \
    python-virtualenv \
    PyYAML \
    rpm-build \
    rubygems \
    sed \
    sshpass \
    subversion \
    sudo \
    unzip \
    which \
    zip \
    && \
    yum clean all

RUN /bin/sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
RUN mkdir /etc/ansible/
RUN /bin/echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts
VOLUME /sys/fs/cgroup /run /tmp
# ssh-keygen -A is not available
RUN ssh-keygen -q -t rsa1 -N '' -f /etc/ssh/ssh_host_key && \
    ssh-keygen -q -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -t ecdsa -N '' -f /etc/ssh/ssh_host_ecdsa_key

COPY requirements.txt /tmp/requirements.txt
RUN pip install -i https://d2c8fqinjk13kw.cloudfront.net/simple/ --disable-pip-version-check -r /tmp/requirements.txt && rm /tmp/requirements.txt

ENV container=docker
CMD ["/sbin/init"]
