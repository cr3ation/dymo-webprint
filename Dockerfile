FROM python:3

# install dymoprint
WORKDIR /
RUN git clone https://github.com/cr3ation/dymoprint.git
WORKDIR /dymoprint
RUN pip3 install --editable .

# install Flask-app
WORKDIR /app
# copy files needed by docker
COPY ["./app/app.py", "docker-entrypoint.sh", "./app/requirements.txt", "docker-entrypoint.sh", "./"]
RUN pip3 install --no-cache-dir -r requirements.txt

# run script to set up default config if non existing, then start
CMD [ "/bin/bash", "/app/docker-entrypoint.sh", "python3", "/app/app.py" ]