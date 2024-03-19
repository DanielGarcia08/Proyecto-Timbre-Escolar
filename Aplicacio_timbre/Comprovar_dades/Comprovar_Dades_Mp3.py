
# Importarem les llibreries necessaries per poder fer aquest projecte (Es important instal·lar-les abans)
# Time, connector MySQL, os, pygame, date
import mysql.connector
import time
import os
import pygame
from datetime import date


# ////AQUEST FITXER, S'UTILITZARA AMB EL CRON, EL DIMONI L'EXECUTARA CADA MINUT 
# PER COMPROVAR SI HI HA ALGUNA HORA PROGRAMADA, DIA FESTIU I REPRODUCCIO DEL FITXER MP3////

# Farem una connexio a la base de dades bdd_timbre del MySQL
Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
# Utilitzarem el Cursor
Cursor_MySQL = Connexio_MySQL.cursor()
# Executarem la Select en que: Ens sortira les dades del Mp3; si es la hora exacta actual i si es el dia exacte actual
Select_Dia_Hora_Exacte = Cursor_MySQL.execute("SELECT ID, Dies, date_format(Hora, '%H:%i') AS Hora, Duracio_Segons, Audio FROM mp3 WHERE Hora = DATE_FORMAT(NOW(),'%H:%i') AND Dies = DAYNAME(NOW())")

# Farem un fetch de totes les files del select
Resultat_Select = Cursor_MySQL.fetchall()



# Utilitzarem un altre cursor perque farem una altre select
Cursor_MySQL_2 = Connexio_MySQL.cursor()
# Executarem la select en que ens seleccionara les dates de dies festius que hi han guardades
Select_Dies_Festius = Cursor_MySQL_2.execute("SELECT ID, DATE_FORMAT(Dies_Festius,'%d-%m-%Y') AS Dies_Festius FROM festius")
# Farem un fetch de totes les files del select
Resultat_Select2 = Cursor_MySQL_2.fetchall()
# Guardarem en una variable un set en que recorreixi les files de la Select, per tenir-ho guardat i ems tard utilitzar-ho
Festius = set([Fila[1] for Fila in Resultat_Select2])

# Farem que el sistema operatiu ens guardi en una llista els fitxers que hi han en el següent directori
Audio_Real = str(os.listdir("/home/ricard/Música"))

# Agafarem la data d'avui
Dia_Actual = date.today()
# Formatarem la data en dias, mesos y any
Format_Data = Dia_Actual.strftime('%d-%m-%Y')

# Fem un for en que es recorreixi les files del select1
for Fila in Resultat_Select:
    # Una vegada obtingut els valors del select1, farem un if si la data actual no hi es en les dates dels dies festius, doncs pasem a la següent condicio
    if Format_Data not in Festius:
        # Si la Fila 4 que es el audio dels audios que hi ha en la taula Mp3, si coincideix un valor que estigui dins del directori
        if Fila[4] in Audio_Real:
            # Iniciem el pygame, per jugar amb fitxers audio
            pygame.mixer.init()  
            # Vull que hem carguis el fitxer Mp3 on es en el directori que els guardo i selecciono el audio de la taula Mp3
            pygame.mixer.music.load("/home/ricard/Música/"+Fila[4])
            # Pygame hem reproduira el fitxer Mp3, que coincideix amb el meu directori
            pygame.mixer.music.play()
            # Fem un time sleep dels segons que volem que duri el audio Mp3
            time.sleep(Fila[3])
            # Quan pasi els segons es parara el reproductor de musica pygame
            pygame.mixer.music.stop()


    else:
        print('Avui es festiu')

   

# Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
Connexio_MySQL.commit()
# Tanquem connexio MySQL
Cursor_MySQL_2.close()
Cursor_MySQL.close()
