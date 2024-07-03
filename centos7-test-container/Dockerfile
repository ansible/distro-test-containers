FROM quay.io/ansible/centos7-test-container:6.3.0

RUN sed -i \
  -e 's/mirrorlist/#mirrorlist/g' \
  -e 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' \
  /etc/yum.repos.d/CentOS-*
