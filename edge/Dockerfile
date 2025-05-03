# Dockerfile
# Production image for AIr4LifeOnTheEdge edge node

FROM python:3.9-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Production Stage ---
FROM python:3.9-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \  # Replaced curl with wget for healthchecks
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1001 -s /bin/bash edgeuser

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Set ownership and permissions
RUN chown -R edgeuser:edgeuser /app && \
    chmod -R 755 /app && \
    chmod +x /app/entrypoint.sh

# Switch to non-root user
USER edgeuser

# Healthcheck using wget
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD wget -q --spider http://localhost:5000/health || exit 1

# Gunicorn configuration
ENV GUNICORN_WORKERS=4 \
    GUNICORN_TIMEOUT=120

# Entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

