FROM python:3.12

WORKDIR /

# Install labelle CLI without dependencies and then install dependencies needed for the CLI
RUN python -m pip install --upgrade pip && \
    pip install --no-deps labelle && \ 
    pip install platformdirs "Pillow>=8.1.2,<11" "PyQRCode>=1.2.1,<2" "python-barcode>=0.13.1,<1" "pyusb" "darkdetect" "typer"

# Install USB-support for python
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y libusb-1.0-0-dev

# Flask-app
WORKDIR /app
# Copy files needed by docker
COPY ["./app/app.py", "docker-entrypoint.sh", "./app/requirements.txt", "docker-entrypoint.sh", "./"]
RUN pip3 install --no-cache-dir -r requirements.txt

# Run script to set up default config if non existing, then start
CMD [ "/bin/bash", "/app/docker-entrypoint.sh", "python3", "/app/app.py" ]
