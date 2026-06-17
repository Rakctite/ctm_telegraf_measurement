FROM telegraf:1.38.4

LABEL org.opencontainers.image.title="ctm_telegraf"
LABEL org.opencontainers.image.version="2.0.3"

USER root

RUN if command -v apk >/dev/null 2>&1; then \
      apk add --no-cache python3 py3-psycopg2; \
    else \
      apt-get update \
      && apt-get install -y --no-install-recommends python3 python3-psycopg2 \
      && rm -rf /var/lib/apt/lists/*; \
    fi

COPY telegraf.conf /etc/telegraf/telegraf.conf
COPY telegraf_py /telegraf/telegraf_py

RUN find /telegraf/telegraf_py -type d -name __pycache__ -prune -exec rm -rf {} + \
    && chmod 0644 /etc/telegraf/telegraf.conf /telegraf/telegraf_py/*.py

CMD ["telegraf", "--config", "/etc/telegraf/telegraf.conf"]
