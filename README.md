# RasPiLoRaRelaySwitch

This project switches on or off some electrical stuff if an according command is received through [Reticulum](https://reticulum.network)'s  [lxmf](https://github.com/markqvist/LXMF). 
In this case we are switching on or off a [Meshcom](https://icssw.org/meshcom/) node in case it goes rogue. You can of course switch anything you like. 
Some optional elements are added to give it something useful to do while not switching something on or off.

This is by no means an out-of-the-box solution but can be very helpful if you want to build a reticulum controlled switch. Depending on your rns config you can make it accessible from all over the world in a reliable manner.

**This guide might also be helpful to you if you just want to make use of a relay with a Raspberry Pi.**

Script (example_receiver.py) based on [The one and only, glad to mention him, most brilliant genius who tired himself to full and utter exhaustion just to bring us this most incredible and noteworthy brilliant solutions exceeding every intellect in this and most probably every other world that might exist somewhere et cetera et cetera](https://github.com/markqvist/LXMF/tree/master/docs)

## Motivation
Since there is already a similar solution out there using [Meshtastic](https://meshtastic.org/) you might ask why reinvent the wheel? 
1. Choosing this you can switch off or on your Meshcom-Node or anything else powered by any current the used relay can handle knowing that your on/off command has reached it's destination.
2. Access your relay switch from everywhere around the globe via the internet using [sideband](https://github.com/markqvist/Sideband)   on your mobile phone or your laptop or [meshchat](https://github.com/liamcottle/reticulum-meshchat) from your laptop/pc or more nerdy/manly stuff like [nomadnet](https://github.com/markqvist/nomadnet) or even more nerdy [lxmf](https://github.com/markqvist/lxmf) on console or python script. 
3. You can query the status (on or off) at any time - in case you forgot or you are not sure if switching worked or not.
4. You can implement any command/code you like to execute.
5. Encryption is not broken (yet).
6. You do not have to compile any (meshtastic-) firmware - it's all out there ready to use.
7. You can improve your karma score by doing something useful with reticulum; you will be one of the chosen few.

## Materials Used
* Raspberry Pi Zero2W (minimal installation)
* Heltec V3 flashed as [RNode](https://github.com/markqvist/RNode_Firmware)
* __5V__ relay __module__
* 1k resistor
* transistor 2N2222
* official RasPi usb-psu (powerful enough)
You might want to use a logic level converter instead of a transistor. 

## Putting Things Together
* RasPi is powered via usb.
* RNode is connected to RasPi using 2nd usb port. 
* Connected to NO-port at the relay module to keep everything working if this circuit breaks down.
* Used the 5V pins on the RasPi since they should be directly connected to the psu. Would not recommend using 3.3V since it might be a bit to much for the RasPi; works but might not do so for a longer period of time. 
* Adapt things to your needs or simply use it partial; e.g. how to connect a relay to a Raspberry Pi or alike.

![Assembly](/WaTu_Schalter_bb.png)

## Installation
Install pip
```bash
sudo apt install pip
```
__optional__
Install fortune
```bash
sudo apt install fortune-mod
```
install rns: [official documentation](https://reticulum.network/manual/gettingstartedfast.html) You might want to install rns as a system service following the link to the official documentation. Or don't if you will not reboot the device ever.
```bash
pip install rns --break-system-packages
```
install lxmf [lxmf](https://github.com/markqvist/LXMF) Don't use pipx, we will need to import the libraries within our python script. You might want to start lxmf as a system service also. 
```bash
pip install lxmf --break-system-packages
``` 
Alter 'example_receiver.py' according to your installation.

Put 'example_receiver.py' into your home directory.

Make the rnsd, lxmd and this script available as a system service or start it manually if you just want to test it out. 

Create a .env File using the example provided in this repo. Put it in your home directory.

## Usage
Send an lxmf message with the secret defined in your .env file to your node. Check the status of your node sending the appropriate lxmf message. Just send a message and enjoy the reply containing your help-text. Go outside and enjoy.

## Maintenance
All this reticulum stuff is challenged in stability and documentation, not to mention the lack of features like groupchats and alike. It is also evolving at a pace that only could impress people in danger of being run over by the movement of a glacier.
So what I did is reboot everything in a regular fashing using cron.
If something goes wrong start the script manually instead of running it as a service and you will presented with error messages you can work with.

## Prose
We are currently using [rnsh](https://github.com/acehoss/rnsh) to administrate the Raspberry Pi using rns. It surprisingly works really well. 

To test things out you might want to use 'screen' on your RasPi.

It might be worth a thought to configure your setup as a transport and propagation node to avoid it being bored.

Please be aware that I am by no means an expert in any of this so please be kind if you destroy things building or using your reticulum switch. __No refunds being made__.

Please use the provided links to install rns and lxmf on your RasPi. Please use the search engine of your choice for help setting up system services. I am glad to provide my humble efforts if needed though.



