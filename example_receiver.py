# used original example script from https://github.com/markqvist/LXMF/tree/master/docs

import RNS
import LXMF
import os, time
import subprocess
from gpiozero import OutputDevice
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 
# relay input pin
relay_pin = 17 
# Initialize relay object
relay = OutputDevice(relay_pin)
relay.off()
reply = "ResponseString"
# In case of NO Relay
zustand = "Meshcom ON"

required_stamp_cost = 8
enforce_stamps = False

def delivery_callback(message):
  global my_lxmf_destination, router, zustand, reply
  time_string      = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(message.timestamp))
  signature_string = "Signature is invalid, reason undetermined"
  if message.signature_validated:
    signature_string = "Validated"
  else:
    if message.unverified_reason == LXMF.LXMessage.SIGNATURE_INVALID:
      signature_string = "Invalid signature"
    if message.unverified_reason == LXMF.LXMessage.SOURCE_UNKNOWN:
      signature_string = "Cannot verify, source is unknown"

  if message.stamp_valid:
    stamp_string = "Validated"
  else:
    stamp_string = "Invalid"

  RNS.log("\t+--- LXMF Delivery ---------------------------------------------")
  RNS.log("\t| Source hash            : "+RNS.prettyhexrep(message.source_hash))
  RNS.log("\t| Source instance        : "+str(message.get_source()))
  RNS.log("\t| Destination hash       : "+RNS.prettyhexrep(message.destination_hash))
  RNS.log("\t| Destination instance   : "+str(message.get_destination()))
  RNS.log("\t| Transport Encryption   : "+str(message.transport_encryption))
  RNS.log("\t| Timestamp              : "+time_string)
  RNS.log("\t| Title                  : "+str(message.title_as_string()))
  RNS.log("\t| Content                : "+str(message.content_as_string()))
  RNS.log("\t| Fields                 : "+str(message.fields))
  if message.ratchet_id:
    RNS.log("\t| Ratchet                : "+str(RNS.Identity._get_ratchet_id(message.ratchet_id)))
  RNS.log("\t| Message signature      : "+signature_string)
  RNS.log("\t| Stamp                  : "+stamp_string)
  RNS.log("\t+---------------------------------------------------------------")

  if message.content_as_string() == (os.getenv("MY_KEY_ON")):
    print("Meshcom ON received!")
    relay.off()
    reply = "Meshcom ON."
    zustand = "Meshcom ON."
  elif message.content_as_string() == (os.getenv("MY_KEY_OFF")):
    print("Meshcom OFF received!")
    relay.on()
    reply = "Meshcom OFF."
    zustand = "Meshcom OFF."
  elif ("help" in (message.content_as_string())):
    reply = "This is your fancy helptext."
  elif ("ustand" in (message.content_as_string())):
    reply = zustand
  elif message.content_as_string() == ("rnstatus"):
    reply = subprocess.getoutput("/home/user/.local/bin/rnstatus")
  # optional send fortune cookie because it's fun!
  # elif ("fortune" in (message.content_as_string())):
  #   reply = subprocess.getoutput("/usr/games/fortune de")
  else: 
    reply = "I did not get you. Try:\"help\" for help."

  # Send a reply
  source = my_lxmf_destination
  dest = message.source
  lxm = LXMF.LXMessage(dest, source, reply, None, desired_method=LXMF.LXMessage.DIRECT, include_ticket=True)
  router.handle_outbound(lxm)

r = RNS.Reticulum()

router = LXMF.LXMRouter(storagepath="/home/user/.lxmd/storage", enforce_stamps=enforce_stamps)
#identity = RNS.Identity()
# eigentliche identity statt zufälliger:
identity = RNS.Identity.from_file("/home/user/.lxmd/identity")
# idfile = os.path.join("/home/user/.lxmd/", "identity")
my_lxmf_destination = router.register_delivery_identity(identity, display_name="RetiSwitch", stamp_cost=required_stamp_cost)
router.register_delivery_callback(delivery_callback)

RNS.log("Ready to receive on: "+RNS.prettyhexrep(my_lxmf_destination.hash))


# You can set a propagation node address to test receiving
# messages from a propagation node, instead of directly

# router.set_outbound_propagation_node(bytes.fromhex("e75d9b6a69f82b48b6077cf2242d7499"))


# This loop allows you to execute various actions for testing
# and experimenting with the example scripts.
while True:
  #input()
  RNS.log("Announcing lxmf.delivery destination...")
  router.announce(my_lxmf_destination.hash)
  time.sleep(600)

  # input()
  # RNS.log("Requesting messages from propagation node...")
  # router.request_messages_from_propagation_node(identity)
