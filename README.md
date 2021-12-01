# Dymo webprint

A web service running in docker used for printing with Dymo LabelManager PnP.

Print using POST request:
```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"text1": "First row", "text2": "Second row", "qr": "https://tiny-url.com"}' \
  http://localhost:5000/print
```

Supported parameters. `text1` is mandatory, rest is optional.
```json
{
    "text1": "First row",
    "text2": "Second row",
    "text3": "Third row",
    "text4": "Forth row",
    "img_url": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    "qr": "https://tiny-url.com",
}
```

## Installation
A Ubuntu/Debian host machine running docker is needed for dymo-webprint to work.

1) On the host machine, copy modeswitch settings to switch LabelManager PnP from beeing recognized as USB storage device, to be recognized as a printer.
```shell
sudo cp 91-dymo-labelmanager-pnp.rules /etc/udev/rules.d/
sudo cp dymo-labelmanager-pnp.conf /etc/usb_modeswitch.d/
```
2) Restart services with:
```shell
sudo systemctl restart udev.service
```
3) Finally, physically disconnect and reconnect the LabelManager PnP [(more info)](http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=947).
4) Continue to "Docker" for setting up the web service.


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

### Volumes
* `/app/` - Entire project including logs

### Useful File Locations (inside container)
* `/app/app.py` - Main webservice
* `/dymoprint/` - Tool for managing printing

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/client-jamf-api/contributors) who
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
