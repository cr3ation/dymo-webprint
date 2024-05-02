# Dymo webprint

A web service running in docker used for printing with Dymo LabelManager PnP. Based on Flask and [labelle](https://github.com/labelle-org/labelle).

Print using POST request:
```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"text1": "First row", "text2": "Second row", "qr": "https://tiny-url.com"}' \
  http://localhost:5001/print
```

Supported parameters. One of either `text1`, `qr` or `img_url` is mandatory, rest is optional.
```json
{
    "text1": "First row",
    "text2": "Second row",
    "text3": "Third row",
    "text4": "Forth row",
    "img_url": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    "qr": "https://tiny-url.com"
}
```

## Installation
### Ubuntu/Debian 

1) On the host machine, download repository and update modeswitch settings to switch LabelManager PnP from beeing recognized as USB storage device, to be recognized as a printer.
```shell
# Clone GitHub repo
git clone https://github.com/cr3ation/dymo-webprint.git

# Move to folder
cd dymo-webprint

# Modeswitch settings to switch LabelManager PnP from beeing recognized as USB storage device, to be recognized as a printer.
echo 'ACTION=="add", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0922", ATTRS{idProduct}=="1001", MODE="0666"' | sudo tee /etc/udev/rules.d/91-labelle-1001.rules

# Restart services
sudo systemctl restart udev.service
```
2) Physically disconnect and reconnect the LabelManager PnP [(more info)](http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=947).
3) Finally, build and run image
```shell
docker compose up
```


## Docker
It's recommended to use `docker compose up` (see installation section above). If you manually want to build and run the container, below are the required steps.

### Prerequisities
In order to build and run you'll need docker installed.
* [Install docker](https://docs.docker.com/engine/install/)

### Build and run  
1) Build image:
```shell
docker build -t dymo-webprint:latest .
```
2) Run container:
```shell
sudo docker run -d --privileged -v /dev/bus/usb:/dev/bus/usb -p 5001:5001 dymo-webprint:latest
```

### Useful File Locations (inside container)
* `/app/app.py` - Main webservice
* `labelle` - Tool for managing printing

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.
Special thanks to the [labelle](https://github.com/labelle-org/labelle) team.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/client-jamf-api/contributors) who
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
