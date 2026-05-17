FROM wpilib/ubuntu-base:22.04

COPY robotCode/ /opt/gradle-seed/
RUN cd /opt/gradle-seed \
    && chmod +x gradlew \
    && ./gradlew build --no-daemon

WORKDIR /workspace
CMD ["/bin/bash"]