# CONFIGURACIO RASPBERRY PER FERLA MES SEGURA

- Canviar la contrassenya usuari Pi

![imagen](https://user-images.githubusercontent.com/61557739/170242587-ea40e890-07c5-4990-a6d1-b84ffef2fa56.png)

- Canviar la contrassenya usuari root

![imagen](https://user-images.githubusercontent.com/61557739/170242689-90600e9a-245c-4f01-b49e-0bc537c1af6a.png)

# CREACIO USUARI ricard

![imagen](https://user-images.githubusercontent.com/61557739/170242782-16e6de78-c0d6-44af-9ab0-e55c69c6bb18.png)

- Li donarem permisos al usuari ricard

![imagen](https://user-images.githubusercontent.com/61557739/170242919-7faf8371-808d-4277-a921-1cc7b6b5d975.png)

# DEMANAR CONTRASSENYA ALS USUARIS QUAN UTILITZIN sudo

- ruta fitxer configuracio usuari pi ---> /etc/sudoers.d/010_pi-nopasswd

![imagen](https://user-images.githubusercontent.com/61557739/170243126-38afbcb4-a470-4d11-a988-822e3938919f.png)

- ruta fitxer configuracio usuari ricard ---> /etc/sudoers.d/010_ricard-nopasswd

![imagen](https://user-images.githubusercontent.com/61557739/170243227-853bc66c-8e86-4ec8-b801-f8a05901b081.png)

- COMPROVACIO DE FUNCIONAMENT

![imagen](https://user-images.githubusercontent.com/61557739/170243289-8684007f-3a66-434d-b276-72b49a742821.png)


# INICIAR AUTOMATICAMENT LA RASPBERRY AMB L'USUARI ricard

- A l'hora d'iniciar la Raspberry farem que ens facin un autologin

- Ruta de configuracio fitxer ---> /etc/lightdm/lightdm.conf

![imagen](https://user-images.githubusercontent.com/61557739/170243583-d79b8229-e1a8-4e44-8b46-36e164062ba9.png)


# COPIA IMATGE SSD RASPBERRY WIN32 DISK IMAGER

- Es necessitara un USB per micro SD

- Tutorial ---> https://www.redeszone.net/2018/03/23/copia-seguridad-micro-sd-raspberry-pi/

![imagen](https://user-images.githubusercontent.com/61557739/170245797-2b372e99-1344-470a-b36e-04f0575fb548.png)

