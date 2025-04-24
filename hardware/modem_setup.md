# LTE Modem Setup (Quectel EC25)

This guide describes how to configure the Quectel EC25 LTE modem for NebulOuS-compliant edge node deployment, enabling public IP connectivity for remote orchestration, real-time data streaming, and predictive maintenance triggers.

## Steps

1. **Insert SIM Card**
   - Use a SIM with a data plan from your mobile provider.

2. **Connect Modem to Raspberry Pi**
   - Plug the Quectel EC25 via USB.

3. **Install Required Packages**

sudo apt update
sudo apt install usb-modeswitch modemmanager network-manager

text

4. **Detect and Activate Modem**
- Check modem is detected:
  ```
  mmcli -L
  ```
- Activate connection (may vary by provider):
  ```
  nmcli con add type gsm ifname "*" con-name lte apn <your_apn>
  nmcli con up lte
  ```

5. **Confirm Public IP**
- Check IP assignment:
  ```
  curl ifconfig.me
  ```
- Ensure the IP is public (not in a private range).

6. **(Optional) Dynamic DNS**
- If your provider assigns a dynamic IP, use a DDNS service (e.g., DuckDNS, No-IP) for stable remote access.

7. **Open Required Ports**
- Use `ufw` or your router to open necessary ports (e.g., 1883 for MQTT, 22 for SSH, any ports required by NebulOuS).

## NebulOuS & Predictive Maintenance

- This setup enables NebulOuS Meta-OS to orchestrate, monitor, and scale edge nodes over public networks.
- Public IP/LTE connectivity is essential for both real-time sensor-driven actions and predictive (Copernicus/forecast-based) triggers, ensuring the edge node can receive orchestration commands at any time.

## Troubleshooting

- If you do not receive a public IP, check with your mobile provider about APN settings and NAT/firewall policies.
- For persistent connectivity, configure NetworkManager to auto-reconnect on boot.

## References

- For hardware specs, see `edge_node_specs.txt`.
- For predictive maintenance integration, see `/predictive_maintenance/`.
