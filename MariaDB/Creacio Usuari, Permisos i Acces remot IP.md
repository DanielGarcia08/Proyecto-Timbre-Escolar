# Creacio Usuari ricard en localhost
- CREATE USER  'ricard '@'localhost' IDENTIFIED BY 'dRxN$=6bqeT=';

- GRANT ALL ON bdd_timbre.* to 'ricard'@'localhost' IDENTIFIED BY 'dRxN$=6bqeT=' WITH GRANT OPTION;

- FLUSH PRIVILEGES;

![imagen](https://user-images.githubusercontent.com/61557739/170239660-e9753ab2-644f-44a8-b30e-2abff3b4cfb8.png)

# Creacio Usuari ricard amb acces d'Arduino

- CREATE USER  'ricard '@'172.20.20.242' IDENTIFIED BY 'dRxN$=6bqeT=';

- GRANT ALL ON bdd_timbre.* to 'ricard'@'172.20.20.242' IDENTIFIED BY 'dRxN$=6bqeT=' WITH GRANT OPTION;

- FLUSH PRIVILEGES;

![imagen](https://user-images.githubusercontent.com/61557739/170239710-f294d6d4-8e6b-401f-ad0b-4ab13c33b46c.png)


# COMPROVACIO DELS USUARIS

- SELECT host, user FROM mysql.user

![imagen](https://user-images.githubusercontent.com/61557739/170239988-ce5b4924-140e-4559-901a-8ddacdd8a65f.png)
