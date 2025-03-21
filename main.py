from time import sleep

import flet as ft

def main(page: ft.Page): #prende come argomento una nuova pagina che è di tipo ft.Page
    page.bgcolor = "white"

    # 1) scrivere del testo. -- OUT
    myText = ft.Text(value="Buongiorno!", color="green", size=30) #costruisce un oggetto di tipo Text che è la visualizzazione di una stringa
    page.controls.append(myText) #aggiungo a questa lista di controlli il mio testo, ma devo aggiornarlo
    page.update() #va a controllare tutti i controlli associati alla pagina e aggiorna i valori

    myCounter = ft.Text(value="")
    page.controls.append(myCounter)
    page.update()


    # 2) creare un campo in cui l'utente può scrivere del testo. -- IN, OUT
    txtIn = ft.TextField(label="Nome", value="Letizia", color="green", disabled=False) #con disbaled=True blocco il campo per impedire che venga modificato
    #page.controls.append(txtIn)
    #page.update()
    page.add(txtIn) #con add() facciamo entrambe le operazioni aggiungo alla lista controlli e aggiorno i controlli
    # page.add(txtIn) # equivale a page.controls.append seguito da page.update

    # 3) creare dei bottoni. Alla pressione di un bottone, eseguo del codice. -- IN
    def handleBtnSaluta(e): #e è un oggetto di tipo Evento che contiene tutte le informazioni rilevanti
        txtOut.value = f"Ciao {txtIn.value}"
        page.update()
    btnSaluta = ft.ElevatedButton(text="Saluta", on_click=handleBtnSaluta, bgcolor="green", color="white") #quando viene cliccato chiama quel metodo
    txtOut = ft.Text(value="Come ti chiami?", color="black")#testo affianco al tasto
    row3 = ft.Row(controls=[btnSaluta, txtOut]) #visualizzo i comandi sulla stessa linea
    page.add(row3)


    # 4) creare un menù a tendina. -- IN
    dd = ft.Dropdown(label="Opzioni", hint_text="Seleziona opzione", options=[ft.dropdown.Option("Opzione 1"), ft.dropdown.Option("Opzione 2")])
    for i in range(3, 20):
        dd.options.append(ft.dropdown.Option(f"Opzione {i}"))
    page.add(dd)


    # 5) visualizzare lunghi elenchi di testo. -- OUT
    def handleAddLV(e):
        if txtIn2.value == "":
            lv.controls.append(ft.Text("Errore. Aggiungi una stringa valida nel campo", color="red"))
            page.update()
        else:
            lv.controls.append(ft.Text(txtIn2.value, color="black"))
            page.update()
    txtIn2= ft.TextField(label="Stringa input", color="black")
    btnIn2 = ft.CupertinoButton(text="Aggiungi a Listview", bgcolor="blue", color="black", on_click=handleAddLV)
    row5 = ft.Row(controls=[txtIn2, btnIn2], alignment=ft.MainAxisAlignment.CENTER)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    page.add(row5, lv)


    #del metodo 1)
    for i in range(100): #è meglio definire tutti i campi grafici e e poi aggiornali dopo
        myCounter.value = f"Counter: {i}"
        myCounter.color = ft.colors.random()
        page.update() #aggiorno la pagina ogni volta che modifico un singolo controllo
        sleep(1) #dice di aspettare un secondo #metodo lella libreria time


ft.app(target=main, view=ft.AppView.FLET_APP) #richiesta di riservare una nuova finestra e chiama il metodo main per riempire la finestra
#argomento di default di view che crea una finestra vuota #view=ft.AppView.FLET_APP
#alternativa #view=ft.AppView.WEB_BROWSER
