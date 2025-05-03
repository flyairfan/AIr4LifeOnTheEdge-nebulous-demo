# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository into the container.
# (If your edge-related files are contained in subfolders like drone_control, server, and simulation, this copies them in.)
COPY . .

# Expose the port on which the Flask server will run.
EXPOSE 5000

# Set the default command to run the Flask server.
CMD [ "python", "server/edge_command_server.py" ]
