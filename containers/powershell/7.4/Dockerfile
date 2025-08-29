FROM public.ecr.aws/docker/library/ubuntu:noble-20250716

# Prevent automatic apt cache cleanup, as caching is desired when running integration tests.
# Instead, when installing packages during container builds, explicit cache cleanup is required.
RUN rm /etc/apt/apt.conf.d/docker-clean

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    libicu74 \
    locales \
    openssh-client \
    openssh-server \
    python-is-python3 \
    systemd-sysv \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Perform locale generation now that the locales package is installed.
RUN locale-gen en_US.UTF-8

# Install PowerShell using a binary archive.
# This allows pinning to a specific version, and also brings support for multiple architectures.
RUN version="7.4.11" && \
    major_version="$(echo ${version} | cut -f 1 -d .)" && \
    install_dir="/opt/microsoft/powershell/${major_version}" && \
    tmp_file="/tmp/powershell.tgz" && \
    arch="$(uname -i)" && \
    arch=$(if [ "${arch}" = "x86_64" ]; then echo "x64"; \
         elif [ "${arch}" = "aarch64" ]; then echo "arm64"; \
         else echo "unknown arch: ${arch}" && exit 1; fi) && \
    url="https://github.com/PowerShell/PowerShell/releases/download/v${version}/powershell-${version}-linux-${arch}.tar.gz" && \
    echo "URL: ${url}" && \
    curl -sL "${url}" > "${tmp_file}" && \
    mkdir -p "${install_dir}" && \
    tar zxf "${tmp_file}" --no-same-owner --no-same-permissions -C "${install_dir}" && \
    rm "${tmp_file}" && \
    find "${install_dir}" -type f -exec chmod -x "{}" ";" && \
    chmod +x "${install_dir}/pwsh" && \
    ln -s "${install_dir}/pwsh" /usr/bin/pwsh && \
    pwsh --version

CMD ["/sbin/init"]
