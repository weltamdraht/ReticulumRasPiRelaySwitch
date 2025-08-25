# RaspiLoRaRelaySwitch
 
This project switches on or off some electrical stuff if an according command is received through [Reticulum](https://reticulum.network)'s  [lxmf](https://github.com/markqvist/LXMF). 
In this case we are switching on or off a [Meshcom](https://icssw.org/meshcom/) node in case it goes rouge. You can of course switch anything you like. 
Some optional elements are added to give it something useful to do while not switching something on or off.

## Materials Used
* Raspberry Pi Zero2W (minimum installation)
* Heltec V3 flashed as [RNode](https://github.com/markqvist/RNode_Firmware)
* 5V(!) relay module(!)
* 1k resistor
* transistor 2N2222
* official Raspi usb-psu (powerful enough)
You might want to use a logic level converter instead of a transistor or any other Raspi. 

## Putting Things Together
* Raspi is powered via usb.
* RNode is connected to Raspi using 2nd usb port. 
* Connected to NO-port at the relay module to keep everything working if this circuit breaks down.
* Used the 5V pins on the Raspi since they should be directly connected to the psu. Would not recommend using 3.3V since it might be a bit to much for the Raspi; works but might not do so for a longer period of time. 
* Adapt things to your needs or simply use it partial; e.g. how to connect a relay to a Raspberry Pi or alike.

![Assembly](/WaTu_Schalter_bb.png)

## Installation
Install pip
```bash
sudo apt install pip
```

Install fortune
```bash
sudo apt install fortune-mod
```
install rns: [official documentation](https://reticulum.network/manual/gettingstartedfast.html) You might want to install rns as a system service following the link to the official documentation. Or don't if you will not reboot the device ever.
```bash
sudo apt install rns --break-system-packages
```
install lxmf [lxmf](https://github.com/markqvist/LXMF) Don't use pipx, we will need to import the libraries within our python script. You might want to start lxmf as a system service also. 
```bash
sudo apt install lxmf --break-system-packages
``` 
Alter 'example_receiver.py' according to your installation.

Put 'example_receiver.py' into your home directory.

Make the script available as a system service (example config provided in this repo).

Create a .env File using the example provided in this repo.

## Usage
Send an lxmf message with the secret defined in your .env file to your node. Check the status of your node sending the appropriate lxmf message. Just send a message and enjoy the reply containing your help-text. Go outside and enjoy.



