#!/bin/bash
exec gunicorn \
    --bind 0.0.0.0:5000 \
    --workers ${GUNICORN_WORKERS} \
    --timeout ${GUNICORN_TIMEOUT} \
    --log-level ${GUNICORN_LOG_LEVEL} \
    server.edge_command_server:app
