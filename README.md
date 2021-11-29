# Dymo webprint

A webservice to print using LabelManager PnP

```shell
curl 127.0.0.1:5000/print/$text1
```

## Installation – manually
### Windows
1) Create python3 _venv_ with `virtualenv venv` (install virtualvenv `pip install virtualenv` if missing)
2) Activate with `venv\Scripts\activate`
3) Run `pip install -r requirements.txt` to install required modules.
4) Edit config in `.\app\settings_sample.py` and rename to `.\app\settings.py`.
5) Start `C:\path-to-venv\Scripts\python.exe` with argument `"C:\path\to\app.py"`

### macOS
1) Create python3 _venv_ with `virtualenv venv` (run `pip install virtualenv` if virtualenv is needed)
2) Activate with `source venv\bin\activate`
3) Run `pip install -r requirements.txt` to install required modules.
4) Edit config in `./app/settings_sample.py` and rename to `./app/settings.py`.
5) Create a LaunchAgent in `/Library/LaunchAgents/com.cr3ation.server.plist` and execute `/path/to/app.py`

## Note
Default port is 5000

## Usage Example
Test if server is up and running
```shell
curl 127.0.0.1:5000/print/$text1
```

## Docker
Install using `docker-compose` or by building the image from scratch. Examples below.

### Prerequisities
In order to run within a container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [macOS](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Install using docker-compose
Edit `docker-compose.yaml`. Add `DEVICE`. Then run
```shell
docker-compose up
```

### Install using docker
#### Build image
```shell
docker build -t dymo-webprint:latest .
```

#### Run container
```shell
sudo docker run -d --privileged -v /dev/bus/usb:/dev/bus/usb -p 5000:5000 dymo-webprint:latest
```

```shell
docker run -d --device=/dev/bus/usb/$(lsusb -d 0922:1002 | awk '{print $2 "/" $4}' | sed 's/://g') -p 5000:5000 dymo-webprint:latest
```


### Environment Variables
* `SLACK_TOKEN` - Mandatory
* `SLACK_ICON_URL` - Mandatory
* `SLACK_USER_NAME` - Mandatory

### Volumes
* `/app/` - Entire project including logs

### Useful File Locations (inside container)
* `/app/app.py` - Main application

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/client-jamf-api/contributors) who
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
