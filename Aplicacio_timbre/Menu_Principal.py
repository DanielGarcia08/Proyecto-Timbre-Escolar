

# Importarem els arxius que volem cridar en el Menu_Principal.py, tots els fitxers han d'estar en un mateix directori

from Mecanic import *
from Mp3 import *
from Calendari_Festius import *


# Crearem una finestra
Menu_Principal = customtkinter.CTk() # Crearem la finestra que sera la principal es a dir la administradora, si la tanquem els altres menus es tancaran perque es el pare
Menu_Principal.geometry("1000x600") # Li configurarem una dimensio per la finestra 
Menu_Principal.title("Timbre Institut Sa Palomera") # Titol de la finestra


# Crearem una funcio en que cridarem a la funcio Mecanic del fitxer Mecanic.py
def Timbre_Mecanic():
   
    Mecanic()

    
# Crearem una funcio en que cridarem a la funcio Mp3 del fitxer Mp3.py
def Timbre_MP3():
    
    Mp3()


# Crearem una funcio en que cridarem a la funcio Calendari del fitxer Calendari_Festius
def Calendari_Festiu():

    Calendari()

# Crearem una etiqueta, que sera el titol del menu principal
Etiqueta_Titol_Menu = customtkinter.CTkLabel(Menu_Principal, # Indiquem el nom on sera el widget
                                             text="BENVINGUT, AL MENU PRINCIPAL DEL TIMBRE: INSTITUT SA PALOMERA!", # Indiquem el text que tindra la etiqueta
                                             text_font=("Helvetica",  18, "italic", "bold"), # Nom i mida de la font del text
                                             text_color="orange") # Color del text

# Utilitzarem pack perque ens quedi ordenat un sota el altra 
Etiqueta_Titol_Menu.pack(pady= 15, padx= 20)

# Crearem un boto, que al fer click ens portara cap al fitxer Mecanic.py
Boto_Timbre_Mecanic = customtkinter.CTkButton(Menu_Principal, # Indiquem el nom on sera el widget
                                              text="Timbre Mecanic", # Indiquem el text que tindra el boto
                                              command=Timbre_Mecanic, # Comanda per cridar la funcio del fitxer Mecanic.py, en que veurem el menu del Timbre Mecanic
                                              fg_color="Steelblue3") # Color de fons del boto

# Utilitzarem pack perque ens quedi ordenat un sota el altra i farem que el boto s'expandeix
Boto_Timbre_Mecanic.pack(pady= 40, padx= 35, fill="both", expand= True)

# Crearem un boto, que al fer click ens portara cap al fitxer Mp3.py
Boto_Timbre_Mp3 = customtkinter.CTkButton(Menu_Principal, # Indiquem el nom on sera el widget
                                          text="Timbre MP3", # Indiquem el text que tindra el boto
                                          command=Timbre_MP3, # Comanda per cridar la funcio del fitxer Mp3.py, en que veurem el menu del Timbre Mp3
                                          fg_color="light coral") # Color de fons del boto

# Utilitzarem pack perque ens quedi ordenat un sota el altra i farem que el boto s'expandeix
Boto_Timbre_Mp3.pack(pady= 30, padx= 35,fill="both", expand= True)


# Crearem un boto, que al fer click ens portara cap al fitxer Calendari_Festius.py
Boto_Calendari_Festiu = customtkinter.CTkButton(Menu_Principal, # Indiquem el nom on sera el widget
                                                text="Calendari Dies Festius", # Indiquem el text que tindra el boto
                                                command=Calendari_Festiu, # Comanda per cridar la funcio del fitxer Calendari_Festius.py, en que veurem el menu del Calendari_Festius
                                                fg_color="orange red") # Color de fons del boto

# Utilitzarem pack perque ens quedi ordenat un sota el altra i farem que el boto s'expandeix
Boto_Calendari_Festiu.pack(pady= 30, padx= 35, fill="both", expand= True)

# Executem la finestra pare, la finestra principal de Menu_Copia
Menu_Principal.mainloop()