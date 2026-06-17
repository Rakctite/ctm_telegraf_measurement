FROM btx/ctm_telegraf

CMD ["telegraf" "--config" "/etc/telegraf/telegraf.conf"]
# RUN /bin/sh -c find /telegraf/telegraf_py -type d -name __pycache__ -prune -exec rm -rf {} +     && chmod 0644 /etc/telegraf/telegraf.conf /telegraf/telegraf_py/*.py # buildkit
COPY telegraf_py /telegraf/telegraf_py # buildkit
COPY telegraf.conf /etc/telegraf/telegraf.conf # buildkit
ADD --no-cache python3 py3-psycopg2;     else       apt-get update && apt-get install -y --no-install-recommends python3 python3-psycopg2       && rm -rf /var/lib/apt/lists/*;     fi # buildkit
# RUN /bin/sh -c if command -v apk >/dev/null 2>&1; then       apk add --no-cache python3 py3-psycopg2;     else       apt-get update && apt-get install -y --no-install-recommends python3 python3-psycopg2       && rm -rf /var/lib/apt/lists/*;     fi # buildkit
CMD ["telegraf"]
COPY entrypoint.sh /entrypoint.sh # buildkit
EXPOSE map[8092/udp:{} 8094/tcp:{} 8125/udp:{}]
# RUN /bin/sh -c ARCH= && dpkgArch="$(dpkg --print-architecture)" &&     case "${dpkgArch##*-}" in       amd64) ARCH='amd64';;       arm64) ARCH='arm64';;       armhf) ARCH='armhf';;       armel) ARCH='armel';;       *)     echo "Unsupported architecture: ${dpkgArch}"; exit 1;;     esac &&     wget --no-verbose https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb.asc &&     wget --no-verbose https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb &&     gpg --batch --verify telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb.asc telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb &&     dpkg -i telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb &&     rm -f telegraf_${TELEGRAF_VERSION}-1_${ARCH}.deb* # buildkit
ENV TELEGRAF_VERSION=1.38.4
# RUN /bin/sh -c set -ex &&     mkdir ~/.gnupg;     echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf;     for key in         24C975CBA61A024EE1B631787C3D57159FC2F927 ;     do         gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys "$key" ;     done # buildkit
# RUN /bin/sh -c DEBIAN_FRONTEND=noninteractive apt-get update &&     DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends iputils-ping snmp procps lm-sensors libcap2-bin &&     rm -rf /var/lib/apt/lists/* # buildkit
# RUN /bin/sh -c set -eux; 	apt-get update; 	apt-get install -y --no-install-recommends 		ca-certificates 		curl 		gnupg 		netbase 		sq 		wget 	; 	rm -rf /var/lib/apt/lists/* # buildkit

# Environment variables
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV TELEGRAF_VERSION=1.38.4

# Exposed ports
EXPOSE 8092
EXPOSE 8094
EXPOSE 8125

# Command
CMD ["telegraf","--config","/etc/telegraf/telegraf.conf"]
