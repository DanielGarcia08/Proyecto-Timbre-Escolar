# CONFIGURACIO XARXA RASPBERRY

- Per configurar la xarxa hem d'anar a la següent ruta ---> /etc/wpa_supplicant/wpa_supplicant.conf
```
network={
ssid="XXXX"
psk="XXXX"
}
```
- Despres fem un reboot

# IMPORTANT




- Els pasos anteriors funcionaran, pero si volem asegurar. Despres de fer tot lo anterior.

- Farem la següent comanda ---> sudo raspi-config

- Anirem a "System Options" > "Wireless LAN"

- Finalment un reboot
