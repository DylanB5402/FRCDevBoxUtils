FROM wpilib/ubuntu-base:22.04

ARG ASCOPE_VERSION=v27.0.0-alpha-4

COPY entrypoint.sh /entrypoint.sh

RUN apt-get update && apt-get install -y binutils \
    && pip3 install multipart \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fL "https://github.com/Mechanical-Advantage/AdvantageScope/releases/download/${ASCOPE_VERSION}/advantagescope-lite-${ASCOPE_VERSION}.ipk" -o /tmp/ascope.ipk \
    && cd /tmp \
    && ar x ascope.ipk \
    && tar xzf data.tar.gz \
    && mv usr/local/bin/advantagescope-lite /opt/ascope \
    && rm -rf /tmp/ascope*

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
WORKDIR /workspace
CMD ["/bin/bash"]