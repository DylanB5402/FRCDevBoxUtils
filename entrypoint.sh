#!/bin/bash
cd /opt/ascope && setsid python3 lite_server.py --enable-file-access &
exec "$@"