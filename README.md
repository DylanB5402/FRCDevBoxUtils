Utilities for FRC Dev Boxes

- Start container with `docker compose run --rm --service-ports devbox`
- Once in the container, sim robot code with `HALSIM_EXTENSIONS=halsim_ds_socket gradlew simulateJava`