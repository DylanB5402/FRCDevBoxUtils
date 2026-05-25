#!/bin/bash
cd /opt/advantagescope-lite && setsid python3 lite_server.py > /dev/null 2>&1 &
exec "$@"
