
# Importarem les llibreries necessaries per poder fer aquest projecte (Es important instal·lar-les abans)
# Tkinter, connector MySQL, Customtkinter, time

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import customtkinter
import time




# Crearem una funcio Anomenada Mp3 per despres cridarla en el fitxer: Menu_Principal.py
def Mp3():

    # Crearem una finestra
    Finestra_Mp3 = customtkinter.CTkToplevel() # Creacio finestra de nivell superior administrada per un administrador de finestres (Menu_Principal, del fitxer Menu_Principal.py)
    Finestra_Mp3.resizable(1,1) # Farem que la finestra sigui redimensionable (1,1) indiquen (True, True)
    Finestra_Mp3.geometry("1200x850") # Li configurarem una dimensio per la finestra 
    Finestra_Mp3.title("Timbre Mp3") # Titol de la finestra

    # ////CREACIO DE DOS FRAMES////
    # La creacio d'aquests frames, ens fara molt mes ordenat la distribucio dels Widgets.
    # Uns Widgets aniran a la vora Esquerra i altres aniran a la vora Dreta

    # Configurarem el disseny de la quadricula (2x1)
    Finestra_Mp3.columnconfigure(1, weight=1)
    Finestra_Mp3.rowconfigure(0, weight=1)
   
    # Crearem un Frame, una vora que estigui situtat en la esquerra
    Vora_Esquerra = customtkinter.CTkFrame(master=Finestra_Mp3, # Indiquem el nom on sera el Frame
                                                 width=180) # Indiquem la amplada 
    Vora_Esquerra.grid(row=0, column=0, sticky="nws") # Indiquem la posicio del Frame (fila, columna; posicio del widget utilitzant(nswe))


    # Crearem un Frame, una vora que estigui situtat en la dreta
    Vora_Dreta = customtkinter.CTkFrame(master=Finestra_Mp3) # Indiquem el nom on sera el Frame
    Vora_Dreta.grid(row=0, column=1, sticky="nswe", padx=20, pady=20) # Indiquem la posicio del Frame (fila, columna; espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    

    # ////FRAME VORA_ESQUERRA////

    # Configurarem el disseny de la quadricula (1x11)
    Vora_Esquerra.rowconfigure(0, minsize=10)   # Fila buida amb la mida mínima com a espai
    Vora_Esquerra.rowconfigure(5, weight=1)  # Fila buida com a espai
    Vora_Esquerra.rowconfigure(8, minsize=20)    # Fila buida amb la mida mínima com a espai
    Vora_Esquerra.rowconfigure(11, minsize=10) # Fila buida amb la mida mínima com a espai
    


    
    # Creacio Etiqueta: Menu Timbre Mp3
    Etiqueta_Mp3 = customtkinter.CTkLabel(Vora_Esquerra, # Indiquem el nom on sera el widget
                                            text="Menu Timbre Mp3", # Indiquem el text que tindra la etiqueta
                                            text_font=("Roboto Medium", -16)) # Nom i mida de la font del text en pixels
    Etiqueta_Mp3.grid(row=1, column=0, pady=10, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, espai entre els widgets(pady, padx))
 
    # Creacio Boto: Tancar timbre Mp3
    Boto_Tancar_Mp3 = customtkinter.CTkButton(Vora_Esquerra,  # Indiquem el nom on sera el widget
                                                text="Tancar timbre Mp3", # Indiquem el text que tindra el Boto
                                                fg_color="red", # Definim el color del boto
                                                command=Finestra_Mp3.destroy) # Comanda per destruir i tancar la finestra de nivell superior
    Boto_Tancar_Mp3.grid(row=2, column=0, pady=10, padx=20) # Indiquem la posicio del Boto (fila, columna, espai entre els widgets(pady, padx))


    # ////FRAME VORA_DRETA////

    # Configurarem el disseny de la quadricula (3x7)
    Vora_Dreta.rowconfigure((0, 1, 2, 3), weight=1) # Fila buida com a espai
    Vora_Dreta.rowconfigure(7, weight=10) # Fila buida amb la mida mínima com a espai
    Vora_Dreta.columnconfigure((0, 1), weight=1) # Columna buida com a espai
    Vora_Dreta.columnconfigure(2, weight=0) # Columna buida amb la mida mínima com a espai


    # Creacio variable StringVar, on es guardara els valors String dels RadioButton
    Valor_RadioButton = StringVar()

    # Creacio d'una llista on es guardaran els valors String dels RadioButton
    Llista = []
 
    # Creacio Etiqueta Dies de la Setmana
    Etiqueta_Dies = customtkinter.CTkLabel(Vora_Dreta,  # Indiquem el nom on sera el widget
                                            text="Dies de la Setmana: ") # Indiquem el text que tindra la etiqueta
    Etiqueta_Dies.grid(row=0, column=0, columnspan=1, pady=20, padx=10, sticky="w") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                                    # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Creacio RadioButton Dilluns
    RadioButton_Dilluns = customtkinter.CTkRadioButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                        text="Dilluns", # Indiquem el text que tindra el RadioButton
                                                        variable=Valor_RadioButton,  # Indiquem la Variable que utilitzara
                                                        value="Dilluns") # Indiquem el valor del RadioButton
    RadioButton_Dilluns.grid(row=1, column=0, pady=10, padx=20, sticky="w") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                            # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Creacio RadioButton Dimarts
    RadioButton_Dimarts = customtkinter.CTkRadioButton(Vora_Dreta,  # Indiquem el nom on sera el widget
                                                        text="Dimarts", # Indiquem el text que tindra el RadioButton
                                                        variable=Valor_RadioButton, # Indiquem la Variable que utilitzara
                                                        value="Dimarts") # Indiquem el valor del RadioButton
    RadioButton_Dimarts.grid(row=2, column=0, pady=10, padx=20, sticky="nw") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                             # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Creacio RadioButton Dimecres
    RadioButton_Dimecres = customtkinter.CTkRadioButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                        text="Dimecres", # Indiquem el text que tindra el RadioButton
                                                        variable=Valor_RadioButton, # Indiquem la Variable que utilitzara
                                                        value="Dimecres") # Indiquem el valor del RadioButton
    RadioButton_Dimecres.grid(row=3, column=0, pady=10, padx=20, sticky="nw") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                              # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Creacio RadioButton Dijous
    RadioButton_Dijous = customtkinter.CTkRadioButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                        text="Dijous", # Indiquem el text que tindra el RadioButton
                                                        variable=Valor_RadioButton, # Indiquem la Variable que utilitzara
                                                        value="Dijous") # Indiquem el valor del RadioButton
    RadioButton_Dijous.grid(row=4, column=0, pady=10, padx=20, sticky="nw") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                            # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Creacio RadioButton Divendres
    RadioButton_Divendres = customtkinter.CTkRadioButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                        text="Divendres", # Indiquem el text que tindra el RadioButton
                                                        variable=Valor_RadioButton, # Indiquem la Variable que utilitzara
                                                        value="Divendres") # Indiquem el valor del RadioButton
    RadioButton_Divendres.grid(row=5, column=0, pady=10, padx=20, sticky="nw") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; 
                                                                               # espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

    # Afegirem a la llista els valors dels RadioButton
    Llista.append(Valor_RadioButton)
   
    
    
    
    
    
    
    
    # Creacio Etiqueta Hora sonar Timbre
    Etiqueta_Sonar_Timbre = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                   text="Hora sonar timbre ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Sonar_Timbre.grid(row=0, column=0, columnspan=2, pady=20, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))

    # Creacio Etiqueta Hores
    Etiqueta_Hores = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                            text="Hores: ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Hores.grid(row=1, column=0, columnspan=2, pady=20, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))

    # Creacio Combobox Hores
    Combobox_Hores = ttk.Combobox(Vora_Dreta, # Indiquem el nom on sera el widget
                                  state="readonly", # Indiquem el estat, en aquest cas nomes pot llegir els valors, no ho pot modificar
                                  values=[*range(0,24)], # Indiquem un rang de numeros en aquest cas fara del 0 fins el 23
                                  width=3) # Indiquem la amplada del Combobox
    
    Combobox_Hores.grid(row=2, column=0,columnspan=2, pady=10, padx=20) # Indiquem la posicio del Combobox (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))


    # Creacio Etiqueta Minuts
    Etiqueta_Minuts = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                             text="Minuts: ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Minuts.grid(row=1, column=0, columnspan=3, pady=20, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))

    # Creacio Combobox Minuts
    Combobox_Minuts = ttk.Combobox(Vora_Dreta, # Indiquem el nom on sera el widget
                                   state="readonly", # Indiquem el estat, en aquest cas nomes pot llegir els valors, no ho pot modificar
                                   values=[*range(0,60)], # Indiquem un rang de numeros en aquest cas fara del 0 fins el 59
                                   width=3) # Indiquem la amplada del Combobox

    Combobox_Minuts.grid(row=2, column=0,columnspan=3, pady=10, padx=20) # Indiquem la posicio del Combobox (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))


    

    # Creacio Etiqueta Duracio Fitxer Mp3
    Etiqueta_Duracio_Mp3 = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                  text="Duracio fitxer Mp3 ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Duracio_Mp3.grid(row=0, column=1, columnspan=3, pady=20, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))

    # Creacio Etiqueta Segons
    Etiqueta_Segons_Mp3 = customtkinter.CTkLabel(Vora_Dreta,  # Indiquem el nom on sera el widget
                                                 text="Segons: ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Segons_Mp3.grid(row=1, column=1, columnspan=3, pady=20, padx=10) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))


    # Creacio variable IntVar, on es guardara el valor Int de la Caixa_Segons_Mp3
    Segons_Mp3 = IntVar()

    # Creacio Caixa Segons Duracio Mp3                                            
    Caixa_Segons_Mp3 = customtkinter.CTkEntry(Vora_Dreta, # Indiquem el nom on sera el widget
                                              textvariable=Segons_Mp3, # Indiquem la Variable que utilitzara
                                              width=170) # Indiquem la amplada de la Caixa
    Caixa_Segons_Mp3.grid(row=2, column=1,columnspan=3, pady=10, padx=20) # Indiquem la posicio de la Caixa (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))


    # Creacio Etiqueta TreeView
    Etiqueta_Treeview = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                               text="Events del Timbre Mp3: ") # Indiquem el text que tindra la Etiqueta
    Etiqueta_Treeview.grid(row=6, column=0,columnspan=2 ,pady=10, padx=20) # Indiquem la posicio de la Caixa (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx))
    
    
    
   

    #Configuracio del TreeView
    TreeView = ttk.Treeview(Vora_Dreta, # Indiquem el nom on sera el TreeView 
                            selectmode ='browse')  # Indiquem que volem seleccionar un valor quan li fem click a una dada del TreeView
  
    TreeView.grid(row=7, column=0,columnspan=2 ,pady=10, padx=20) # Indiquem la posicio del TreeView (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx)

    # Definim el Numero de Columnes del Treeview
    TreeView["columns"] = ("1", "2", "3", "4", "5")
    
    # Definim el Encapçalament del TreeView
    TreeView['show'] = 'headings'
    
    # Especifiquem l'Amplada de Columnes i la Seva Alineacio, el anchor es per definir on es posicionara les columnes
    TreeView.column("1", width = 30, anchor ='center')
    TreeView.column("2", width = 170, anchor ='center')
    TreeView.column("3", width = 170, anchor ='center')
    TreeView.column("4", width = 140, anchor ='center')
    TreeView.column("5", width = 160, anchor ='center')

    
    # Encapçalaments del TreeView  
    
    # Posarem els encapçalaments en les seves respectives columnes
    TreeView.heading("1", text ="ID")
    TreeView.heading("2", text ="Dies")
    TreeView.heading("3", text ="Hora")
    TreeView.heading("4", text ="Duracio_Segons")
    TreeView.heading("5", text ="Audio")

     
     
    #Treeview Personalitzat amb colors
    Personalitzacio_TreeView = ttk.Style() # Definim que volem modificar el stil del TreeView
    Personalitzacio_TreeView.theme_use("clam") # Definim el tema que utilitzen en el TreeView
    Personalitzacio_TreeView.configure("Treeview", # Configuracio del stil del TreeView
                                      background="Silver", # Definim el color de fons del TreeView
                                      foreground="black", # Definim el color de text del TreeView
                                      rowheight=25, # Definim l'altura de la fila del TreeView
                                      fieldbackground="silver") # Definim el color de fons del camp del TreeView
    
    # Aqui definim que al fer click a una dada del TreeView ens ho seleccioni i li doni un color
    Personalitzacio_TreeView.map('Treeview',
        background=[('selected', 'DeepSkyBlue4')])



    # ////CREACIO DE FUNCIONS////

    # Crearem una funcio anomenada Mostrar_Dades_Treeview la que ens mostrara les dades de la taula MySQL Mp3 en el TreeView automaticament quan entrem al menu del timbre Mp3
    def Mostrar_Dades_TreeView():

        # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()
        # Executarem la Select de la taula mp3, en la que obtindrem les dades ordenades per dia i hora
        Cursor_MySQL.execute("SELECT * FROM mp3 ORDER BY FIELD(Dies, 'Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres'), Hora ASC ")

        # Farem un fetch de totes les files del select
        Resultat_Select = Cursor_MySQL.fetchall()
            
            
        # Utilitzarem un for per recorre els valors de cada fila i que ens faci un insert d'aquests valors al TreeView
        # Aixi podem veure totes les dades del mp3 en el TreeView
        for Fila in Resultat_Select:
                
            TreeView.insert("", 'end',iid=Fila[0], text=Fila[0],
                values =(Fila[0],Fila[1],Fila[2],Fila[3],Fila[4]))
            
            
        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()
    
    # Cridem a la funcio perque es veguin les dades en el TreeView quan entrem al Menu timbre Mp3
    Mostrar_Dades_TreeView()


    # Crearem una funcio anomenada Rellotge per mostrar les hores, minuts i segons actuals en el Menu timbre Mp3
    def Rellotge():
        # Definim la variable Hora_Rellotge i que ens doni l'hora actual
        Hora_Rellotge = time.strftime("%H")
        # Definim la variable Minuts_Rellotge i que ens doni els minuts actuals
        Minuts_Rellotge = time.strftime("%M")
        # Definim la variable Segons_Rellotge i que ens doni els segons actuals
        Segons_Rellotge = time.strftime("%S")

        # Creacio Etiqueta_Resultat
        Etiqueta_Resultat = customtkinter.CTkLabel(Vora_Esquerra, # Indiquem el nom on sera el widget
                                                   text= Hora_Rellotge + ":" + Minuts_Rellotge + ":"+ Segons_Rellotge, # El text sera el resultat de la Hora, Minuts i Segons actuals
                                                   fg_color="plum1", # Definim el color de text de la Etiqueta
                                                   height=70, # Definim la seva alçada
                                                   width=100) # Definim la seva Amplada
        Etiqueta_Resultat.grid(row=5, column=0, pady=10, padx=20, sticky="w") # Indiquem la posicio de la Etiqueta (fila, columna,; espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe))

        #Cridarem la Etiqueta Resultat i la funcio Rellotge perque corri els segons actuals, es a dir perque es vagi actualitzant el temps real actual                                          
        Etiqueta_Resultat.after(1000, Rellotge)
        
    # Cridem la funcio Rellotge perque es mostri en el Menu del Timbre Mp3, en la vora esquerra
    Rellotge()


    


    # Crearem una funcio anomenada Eliminar_Dades_TreeView la que ens eliminara les dades de la taula MySQL mp3 que nosaltres seleccionem en el TreeView
    def Eliminar_Dades_TreeView():
        # Definim la variable en la que contindra el valor seleccionat en el TreeView
        Seleccio_Item = TreeView.selection()[0]
        # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()
        # Fem la comanda Delete del mp3, en la que ens eliminara el ID que nosaltres seleccionem en el TreeView
        Delete_Mp3 = "DELETE FROM mp3 WHERE ID = %s"
        # Guardem la variable Seleccio Item com a Item del TreeView
        Item = (Seleccio_Item, )
        # Executarem la comanda Delete amb el valor Item que es el que seleccionem fent click en el TreeView
        Variable_Delete = Cursor_MySQL.execute(Delete_Mp3, Item)
        
        
        # Si el El item que seleccionem fent click en el Treeview es 1, per tant hem elimines el Valor Item que he seleccionat en el TreeView
        if(Variable_Delete==1):
            TreeView.delete(Seleccio_Item) # S'esborra el item seleccionat en la base de dades
        TreeView.delete(Seleccio_Item) # S'esborra el item seleccionat en el TreeView
      
        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()


    # Crearem una funcio Anomenada Obtenir_Dies, per obtenir els dies que nosaltres seleccionem en el RadioButton
    def Obtenir_Dies():
        # Declarem una variable i obtenim el valor dels dies que nosaltres seleccionem en el Radiobutton
        Valor_Dies = Valor_RadioButton.get()
        # Ens retorni el valor obtingut dels Dies
        return Valor_Dies
       
    # Crearem una funcio Anomenada Obtenir_Duracio_Audio, per obtenir els segons de duracio d'audio que nosaltres posem en la Caixa
    def Obtenir_Duracio_Audio():
        # Declarem una variable i obtenim el valor dels segons que nosaltres posem en la caixa
        Valor_Duracio = Caixa_Segons_Mp3.get()
        
        # Ens retorni el valor obtingut dels segons de d'uracio d'audio
        return Valor_Duracio

    # Crearem una funcio Anomenada Obtenir_Hores, per obtenir les hores i minuts que nosaltres seleccionem en el Combobox_Hores i Combobox_Minuts
    def Obtenir_Hores():
        # Declarem dos variables per obtenir el valor de les Hores i Minuts que nosaltres seleccionem
        Valor_Hores = Combobox_Hores.get()
        Valor_Minuts = Combobox_Minuts.get()

        # Declarem una variable en la que Obtindrem en una String les Hores i minuts. 
        # El zfill s'utilitza per afegir un 0 a la esquerra, en aquest cas a l'hora i minuts. P.E --> en comptes de les: 5:4h, serian les: 05:04h
        Hora = str(Valor_Hores).zfill(2) + ':' + str(Valor_Minuts).zfill(2)
    
        # Ens retorni el valor obtingut en format de la Hora
        return Hora

   

    # Crearem una funcio Anomenada Seleccionar_Fitxer_Mp3, per seleccionar el Fitxer Mp3 que nosaltres volguem
    def Seleccionar_Fitxer_Mp3():
        # Declarem una variable global, ja que necesitarem la variable Nom_Fitxer_Audio en una altre funcio, en la funcio: Obtenir_Fitxer_Mp3
        global Nom_Fitxer_Audio
        # Declarem una variable en la que s'obrira una finestra per seleccionar el Fitxer Mp3
        Nom_Fitxer_Audio = filedialog.askopenfilename(initialdir="/home/ricard/Música", # Posem el directori on volem que s'obri directament la finestra, per seleccionar el nostre fitxer Mp3
                                                      title="Selecciona un fitxer Mp3") # Titol de la finestra
        # Al obrir la finestra per seleccionar el Fitxer Mp3 lo que fara es que el Menu (Menu_Principal, del fitxer Menu_Principal.py) s'amagui per que no ens molesti.                                           
        Finestra_Mp3.deiconify()
        
        # Declarem una variable en la que ens suprimira la ruta del fitxer i nomes ens quedara el nom del fitxer Mp3.
        # P.E ---> En comptes de: D:/Usuaris/Pepito/Music/alarma.mp3, seria: alarma.mp3
        Titol_Fitxer   = Nom_Fitxer_Audio.split("/")
        Titol_Fitxer   = str(Titol_Fitxer[-1])

        # Creacio Etiqueta_Fitxer_Mp3
        Etiqueta_Fitxer_Mp3 = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                     text="Fitxer Mp3 Escollit:") # Indiquem el text que tindra la Etiquet
        Etiqueta_Fitxer_Mp3.grid(row=0, column=3, columnspan=1, pady=20, padx=10, sticky="we") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe)

        # Creacio Etiqueta_Fitxer_Mp3_Escollit
        Etiqueta_Fitxer_Mp3_Escollit = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                              text=Titol_Fitxer, # Indiquem la Variable del Titol_Fitxer, per obtenir el nom del fitxer Mp3
                                                              fg_color="light goldenrod") # Definim el color de text de la Etiqueta
        Etiqueta_Fitxer_Mp3_Escollit.grid(row=1, column=3, columnspan=1, pady=10, padx=20, sticky="we") # Indiquem la posicio de la Etiqueta (fila, columna; ocupacio de columna; espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe)

        # Retornem Etiqueta_Fitxer_Mp3_Escollit perque ens sorti sempre en pantalla la etiqueta indicant quin fitxer Mp3 hem seleccionat 
        return Etiqueta_Fitxer_Mp3_Escollit


    # Crearem una funcio anomenada Obtenir_Fitxer_Mp3, en la que gracies a la variable Global Nom_Fitxer_Audio
    # Podrem guardar la variable del nom del fitxer Mp3, per mes tard fer un insert a la base de dades en la taula Mp3
    def Obtenir_Fitxer_Mp3():
       
       # Obtenim el nom del fitxer Mp3
        Titol_Fitxer   = Nom_Fitxer_Audio.split("/")
        Titol_Fitxer   = str(Titol_Fitxer[-1])
        
        # Retornem el Valor Titol_Fitxer
        return Titol_Fitxer


    # Crearem una funcio anomenada Inserir_Dades_Timbre_Mp3, en que inserirem a la taula Mp3 del MySQL els valors de les funcions anteriors
    def Inserir_Dades_Timbre_Mp3():
        # Farem una connexio a la base de dades bdd_timbre del MySQL
        Connexio_MySQL = mysql.connector.connect(host='localhost',user='ricard',passwd='dRxN$=6bqeT=',db='bdd_timbre')
        # Utilitzarem el Cursor
        Cursor_MySQL = Connexio_MySQL.cursor()
        # Fem la comanda INSERT INTO en la taula mp3, en la que ens insertara els valors de les funcions
        Insert_Mp3 = "INSERT INTO mp3 (Dies, Hora, Duracio_Segons, Audio) VALUES (%s,%s,%s,%s)"

        # Posarem els valors de les funcions
        Valors_Mp3=(Obtenir_Dies(), Obtenir_Hores(), Obtenir_Duracio_Audio(), Obtenir_Fitxer_Mp3())
        # Executarem la comanda Insert amb el valors Mp3
        Cursor_MySQL.execute(Insert_Mp3, Valors_Mp3)
       
        # Utilitzarem el commit perque ens faci la transaccio de la connexio a la Base de Dades
        Connexio_MySQL.commit()
        # Tanquem connexio MySQL
        Cursor_MySQL.close()


        # Creacio Etiqueta_Resultat_Insert_Mp3
        Etiqueta_Resultat_Insert_Mp3 = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                              text= "Ultim registre programat: "  + Obtenir_Dies() +" "+ Obtenir_Hores() + "h", # El text sera el resultat del Dia i Hora programada
                                                              fg_color="lawn green") # Definim el color de text de la Etiqueta
        Etiqueta_Resultat_Insert_Mp3.grid(row=5, column=2, columnspan=1, pady=10, padx=20) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx)
        
        # Creacio Etiqueta_Resultat_Duracio_Audio_Mp3
        Etiqueta_Resultat_Duracio_Audio_Mp3 = customtkinter.CTkLabel(Vora_Dreta, # Indiquem el nom on sera el widget
                                                                     text= "Duracio i Audio: "  + Obtenir_Duracio_Audio()+ "s" +" "+ Obtenir_Fitxer_Mp3(), # El text sera el resultat de la duracio d'audio i el nom del fitxer mp3
                                                                     fg_color="LightCoral") # Definim el color de text de la Etiqueta
        Etiqueta_Resultat_Duracio_Audio_Mp3.grid(row=6, column=2, columnspan=1, pady=10, padx=20) # Indiquem la posicio de la Etiqueta (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx)
        
        # Fem una caixa de missatge que quan insereixi les dades a la taula del Mp3, ens digui que tot esta correcte
        messagebox.showinfo ("Event Programat", "El teu registre s'ha programat correctament")

        # Al sortir la caixa de missatge fara que el Menu (Menu_Principal, del fitxer Menu_Principal.py) s'amagui per que no ens molesti
        Finestra_Mp3.deiconify()

    # Creacio Boto: Afegir Event
    Boto_Afegir_Event = customtkinter.CTkButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                text='Afegir Event', # Indiquem el text que tindra el Boto
                                                command=Inserir_Dades_Timbre_Mp3) # Comanda per inserir les dades del timbre Mp3
    
    Boto_Afegir_Event.grid(row=7, column=2, columnspan=1, pady=10, padx=20) # Indiquem la posicio del Boto (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx)

    # Creacio Boto: Seleccionar Fitxer Mp3
    Boto_Seleccionar_Mp3 = customtkinter.CTkButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                                   text='Seleccionar Fitxer Mp3', # Indiquem el text que tindra el Boto
                                                   fg_color="SeaGreen1", # Definim el color del boto
                                                   command=Seleccionar_Fitxer_Mp3) # Comanda per Obrir i mostrar el Fitxer_Mp3 Seleccionat
    

    Boto_Seleccionar_Mp3.grid(row=2, column=3, columnspan=1, pady=10, padx=20, sticky="we") # Indiquem la posicio del Boto (fila, columna; ocupacio de columna; espai entre els widgets(pady, padx); posicio del widget utilitzant(nswe)

    # Creacio Boto: Eliminar Event
    Boto_Eliminar = customtkinter.CTkButton(Vora_Dreta, # Indiquem el nom on sera el widget
                                            text='Eliminar Event', # Indiquem el text que tindra el Boto
                                            fg_color="red", # Definim el color del boto
                                            command=Eliminar_Dades_TreeView) # Comanda per eliminar les dades del timbre Mp3 i del TreeView
        
    
    Boto_Eliminar.grid(row=8, column=0,columnspan=2 ,pady=10, padx=20) # Indiquem la posicio del Boto (fila, columna, ocupacio de columna; espai entre els widgets(pady, padx)

    # Executem la finestra de nivell superior dins del Menu Mp3
    Finestra_Mp3.mainloop()





