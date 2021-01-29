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
    mercurial \
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

RUN pip install 'cryptography==1.9' 'pycparser==2.18' 'cffi==1.14.3' 'packaging==16.8'

RUN /bin/sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
RUN mkdir /etc/ansible/
RUN /bin/echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts
VOLUME /sys/fs/cgroup /run /tmp
RUN ssh-keygen -q -t rsa1 -N '' -f /etc/ssh/ssh_host_key && \
    ssh-keygen -q -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    for key in /etc/ssh/ssh_host_*_key.pub; do echo "localhost $(cat ${key})" >> /root/.ssh/known_hosts; done
RUN pip install 'coverage==4.5.4' 'resolvelib==0.5.4' 'junit-xml==1.9'
ENV container=docker
CMD ["/sbin/init"]
