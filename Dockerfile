FROM wpilib/ubuntu-base:22.04

COPY robotCode/ /opt/gradle-seed/
RUN cd /opt/gradle-seed \
    && chmod +x gradlew \
    && ./gradlew build --no-daemon

COPY AdvantageScope/lite/ /opt/advantagescope-lite/
COPY AdvantageScope/www/ /opt/advantagescope-lite/static/www/
RUN pip3 install multipart==1.3.0

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /workspace
CMD ["/bin/bash"]