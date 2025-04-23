# LTE Modem Setup

1. Insert active SIM card (data plan) into Quectel EC25 modem.
2. Connect modem to Raspberry Pi via USB.
3. Install drivers (`sudo apt install usb-modeswitch modemmanager`).
4. Configure network (e.g., using `mmcli` or NetworkManager).
5. (Optional) Set up Dynamic DNS if public IP is dynamic.
6. Open required ports in firewall/router.

**Result:** NebulOuS platform can reach the edge node via public IP (or port forward).
