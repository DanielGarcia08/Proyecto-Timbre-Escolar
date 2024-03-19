

# Importarem les llibreries necessaries per poder fer aquest projecte (Es important instal·lar-les abans)
# Tkinter, tkcalendar, datetime, mysql.connector, cutomtkinter


from tkinter import *
from tkinter import ttk
from tkcalendar import *
import datetime
import mysql.connector
import customtkinter

# Crearem una funcio Anomenada Calendari per despres cridarla en el fitxer: Menu_Principal.py
def Calendari():

    
    # Crearem una finestra
    Finestra_Calendari = customtkinter.CTkToplevel() # Creacio finestra de nivell superior administrada per un administrador de finestres (Menu_Principal, del fitxer Menu_Principal.py)
    Finestra_Calendari.resizable(1,1) # Farem que la finestra sigui redimensionable (1,1) indiquen (True, True)
    Finestra_Calendari.geometry("1200x850")
    Finestra_Calendari.title('Calendari Dies Festius') # Titol de la finestra

    # Crearem una variable que ens agafi la data d'avui
    Data_Actual = datetime.date.today()


   # Crearem una variable en la que hi sera el calendari, per configurar-ho
    Calendari = Calendar(Finestra_Calendari, # Indiquem el nom on sera la Finestra
                         selectmode="day", # Selecionem el mode que es un dia
                         date_pattern="yyyy-mm-dd", # Seleccionem el format de la data
                         year=Data_Actual.year, # Aqui, farem que ens agafi l'any actual en el calendari
                         month=Data_Actual.month, # Aqui, farem que ens afagi el mes actual en el calendari
                         day=Data_Actual.day, # Aqui, farem que ens agafi el dia actua en el calendari
                         locale="ca_ES") # Seleccionarem el Idioma en Catala del Calendari
    Calendari.pack(fill=BOTH, expand=1,padx=30, pady=30) # Utilitzarem pack perque ens quedi ordenat un sota el altra i volem que s'expandi el calendari


    

   
    #Configuracio del treeview
    TreeView = ttk.Treeview(Finestra_Calendari, # Indiquem el nom on sera el TreeView 
                            selectmode ='browse') # Indiquem que volem seleccionar un valor quan li fem click a una dada del TreeView
  
    TreeView.pack(pady=3) # Utilitzem pack perque el treeview ens quedi sota el calendari

   # Definim el Numero de Columnes del Treeview
    TreeView["columns"] = ("1", "2")
    
    # Definim el Encapçalament del TreeView
    TreeView['show'] = 'headings'
    
    # Especifiquem l'Amplada de Columnes i la Seva Alineacio, el anchor es per definir on es posicionara les columnes 
    TreeView.column("1", width = 30, anchor ='center')
    TreeView.column("2", width = 170, anchor ='center')
  

    
    # Encapçalaments del TreeView  
    
    # Posarem els encapçalaments en les seves respectives columnes
    TreeView.heading("1", text ="ID")
    TreeView.heading("2", text ="Dies_Festius")
    
    #Treeview Personalitzat amb color
    Personalitzacio_TreeView = ttk.Style() # Definim que volem modificar el stil del TreeView
    Personalitzacio_TreeView.theme_use("clam")  # Definim el tema que utilitzen en el TreeView
    Personalitzacio_TreeView.configure("Treeview", # Configuracio del stil del TreeView
                    background="Silver", # Definim el color de fons del TreeView
                    foreground="black", # Definim el color de text del TreeView
                    Filaheight=25, # Definim l'altura de la fila del TreeView
                    fieldbackground="silver") # Definim el color de fons del camp del TreeView
    
    # Aqui definim que al fer click a una dada del TreeView ens ho seleccioni i li doni un color
    Personalitzacio_TreeView.map('Treeview',
        background=[('selected', 'DeepSkyBlue4')])






    

    # Crearem una funcio anomenada Mostrar_Dades_Treeview la que ens mostrara les dades de la taula MySQL Dies_Festius en el TreeView automaticament quan entrem al menu del Calendari_Festius
    def Mostrar_Dades_TreeView():
         # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()
        # Executarem la Select de la taula Dies_Festius, en la que obtindrem les dades ordenades per la data
        Cursor_MySQL.execute("SELECT ID, DATE_FORMAT(Dies_Festius,'%d-%m-%Y') AS Dies_Festius FROM festius ORDER BY Month(Dies_Festius), Dies_Festius ASC ")

        # Farem un fetch de totes les files del select
        Resultat_Select = Cursor_MySQL.fetchall()
            
            
        # Utilitzarem un for per recorre els valors de cada fila i que ens faci un insert d'aquests valors al TreeView
        # Aixi podem veure totes les dades del Calendari_Festius en el TreeView
        for Fila in Resultat_Select:
                
            TreeView.insert("", 'end',iid=Fila[0], text=Fila[0],
                values =(Fila[0],Fila[1]))
            
            
        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()

     # Cridem a la funcio perque es veguin les dades en el TreeView quan entrem al Menu Calendari_Festius    
    Mostrar_Dades_TreeView()

    # Crearem una funcio anomenada Inserir_Dades_Calendari_Festius, en que inserirem a la taula Dies_Festius del MySQL la data que nosaltres seleccionem
    def Inserir_Dades_Calendari_Festius():
        # Crearem una variable en la que si seleccionem una data en el calendari es guardi
        Dia_Festiu = Calendari.get_date()
        Dia_Festiu_trans = Dia_Festiu.split()
        
        # Crearem una etiqueta en que ens sorti la data quan nosaltres li fem click en guardar dia festiu
        Etiqueta_Resultat_Dia_Festiu.config(text="El Dia Festiu: " + Dia_Festiu + " S'ha Guardat correctament", fg_color="green")

        # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
      
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()

        # Fem la comanda INSERT INTO en la taula Festius, en la que ens insertara el valor de la data que nosaltres seleccionem
        Insert_Calendari_Festius = "INSERT INTO festius (Dies_Festius) VALUES (%s)"
        # Posarem els valor del dia que nosaltres seleccionem
        Valors_Calendari_Festius=(Dia_Festiu_trans)

        # Executarem la comanda Insert amb el valors Festius
        Cursor_MySQL.execute(Insert_Calendari_Festius, Valors_Calendari_Festius)

        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()

    # Crearem una funcio anomenada Eliminar_Dades_TreeView la que ens eliminara les dades de la taula MySQL Festius que nosaltres seleccionem en el TreeView
    def Eliminar_Dades_TreeView():
        # Definim la variable en la que contindra el valor seleccionat en el TreeView
        Seleccio_Item = TreeView.selection()[0]
        # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()
        # Fem la comanda Delete dels Festius, en la que ens eliminara el ID que nosaltres seleccionem en el TreeView
        Delete_Calendari = "DELETE FROM festius WHERE ID = %s"
        # Guardem la variable Seleccio Item com a Item del TreeView
        Item = (Seleccio_Item, )
        # Executarem la comanda Delete amb el valor Item que es el que seleccionem fent click en el TreeView
        Variable_Delete = Cursor_MySQL.execute(Delete_Calendari, Item)
         
        # Si el El item que seleccionem fent click en el Treeview es 1, per tant hem elimines el Valor Item que he seleccionat en el TreeView
        if(Variable_Delete==1):
            TreeView.delete(Seleccio_Item) # S'esborra el item seleccionat en la base de dades
        TreeView.delete(Seleccio_Item) # S'esborra el item seleccionat en el TreeView
    
        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()

    # Creacio Boto: Guardar Dia Festiu
    Boto_Guardar_Festiu = customtkinter.CTkButton(Finestra_Calendari, # Indiquem el nom on sera el widget
                                                  text="Guardar Dia Festiu", # Indiquem el text que tindra el Boto
                                                  command=Inserir_Dades_Calendari_Festius) # Comanda per inserir les dades de festius

    Boto_Guardar_Festiu.pack(pady=3) # Utilitzarem pack perque ens quedi ordenat un sota el altra 

    # Creacio Boto: Eliminar Dia Festiu
    Boto_Eliminar_Festiu = customtkinter.CTkButton(Finestra_Calendari, # Indiquem el nom on sera el widget
                                                   text='Eliminar Dia Festiu', # Indiquem el text que tindra el Boto
                                                   fg_color="red", # Definim el color del boto
                                                   command=Eliminar_Dades_TreeView) # Comanda per eliminar les dades de Festius i del TreeView
        
    
    Boto_Eliminar_Festiu.pack(pady=3) # Utilitzarem pack perque ens quedi ordenat un sota el altra 

    # Creacio Etiqueta on sera cridada quan guardem un dia festiu
    Etiqueta_Resultat_Dia_Festiu = customtkinter.CTkLabel(Finestra_Calendari, # Indiquem el nom on sera el widget
                                                          text="")  # Indiquem el text com a buit perque no ens sorti lleig, es a dir que posi CTkLabel
                                                          
    Etiqueta_Resultat_Dia_Festiu.pack( pady=3) # Utilitzarem pack perque ens quedi ordenat un sota el altra

    # Creacio Boto: Tancar Calendari
    Boto_Tancar_Calendari= customtkinter.CTkButton(Finestra_Calendari,  # Indiquem el nom on sera el widget
                                                   text="Tancar Calendari", # Indiquem el text que tindra el Boto
                                                   fg_color="salmon1", # Definim el color del boto
                                                   command=Finestra_Calendari.destroy) # Indiquem que quan fem click aquest boto, la finestra es tancara
    # Utilitzarem pack perque ens quedi ordenat un sota el altra                                               
    Boto_Tancar_Calendari.pack( pady=3)

    # Executem la finestra de nivell superior dins del Menu Calendari
    Finestra_Calendari.mainloop()