# Creacio Base de Dades
- CREATE DATABASE bdd_timbre;
 
![imagen](https://user-images.githubusercontent.com/61557739/170237380-772bc380-e98f-4c0c-8db1-40e47335525a.png)

# Creacio Taula mecanic
```
CREATE TABLE mecanic(
 ID INT NOT NULL AUTO_INCREMENT,
 Dies VARCHAR (20)  NOT NULL,
 Hora TIME NOT NULL,
 PRIMARY KEY (ID));
```
![imagen](https://user-images.githubusercontent.com/61557739/170237499-441534cb-6d08-4c84-8305-d796f5451310.png)



# Creacio Taula mp3
```
CREATE TABLE mp3(
 ID INT NOT NULL AUTO_INCREMENT,
 Dies VARCHAR (20)  NOT NULL,
 Hora TIME NOT NULL,
 Duracio_Segons INT NOT NULL,
 Audio VARCHAR(20) NOT NULL,
 PRIMARY KEY (ID));
```
![imagen](https://user-images.githubusercontent.com/61557739/170237527-054f3c7a-7159-49a2-9919-aaab16a8fc21.png)


# Creacio Taula festius
```
CREATE TABLE festius(
 ID INT NOT NULL AUTO_INCREMENT,
 Dies_Festius DATE  NOT NULL,
 PRIMARY KEY (ID));
```
![imagen](https://user-images.githubusercontent.com/61557739/170237553-ed1d54a6-0076-4756-acd5-82da05a8ee26.png)
